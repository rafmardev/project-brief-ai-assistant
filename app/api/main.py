from typing import List
from core.use_cases.document_query import QueryDocumentUseCase
from infrastructure.gemini.gemini_query_service_dummy import GeminiQueryServiceDummy
from core.domain.entities import BriefResponse, SearchResult, SemanticQuery
from core.use_cases.upload_document import UploadDocumentUseCase
from infrastructure.repositories.local_document_repository import LocalDocumentRepository
from infrastructure.gemini.gemini_uploader_dummy import GeminiUploaderDummy
from config.logging import setup_logging
from fastapi import FastAPI, UploadFile, File, HTTPException

logger = setup_logging()
app = FastAPI()

@app.get("/health")
def read_root():
    return {"health": "ok"}

@app.post(
        "/brief", 
        description="Endpoint for upload project documents")
def generate_brief(files: List[UploadFile] = File(...)):
    if not files:
        return {"error": "No files uploaded."}
    document_repository = LocalDocumentRepository()
    uploader = GeminiUploaderDummy()  # Assuming GeminiUploader is defined elsewhere
    use_case = UploadDocumentUseCase(document_repository=document_repository, uploader=uploader)
    uploaded_documents = use_case.upload(files)
    
    return BriefResponse(
        project_id=uploaded_documents.document.id,
        brief=uploaded_documents.gemini_response.message
    )

# Run semantic queries over the uploaded files
@app.post("/search",
          responses={404: {"description": "Document not found"}},
          description="Endpoint for semantic search over project documents")
def run_search(query: SemanticQuery):
    query_service = GeminiQueryServiceDummy() 
    repository = LocalDocumentRepository()
    try:
        use_case = QueryDocumentUseCase(
            document_query_service=query_service,
            repository=repository)
        
        response = use_case.execute(file_id=query.project_id, prompt=query.query)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Document not found.")
    return SearchResult(results=[
        {
            "file": query.project_id,
            "snippet": response.message
        }
    ])