from typing import List
from config.settings import get_settings
from infrastructure.gemini.gemini_query_service_impl import GeminiQueryServiceImpl
from infrastructure.gemini.gemini_uploader_impl import GeminiUploaderImpl
from core.use_cases.semantic_query import SemanticQueryUseCase
from core.domain.entities import BriefResponse, SearchResult, SemanticQuery
from core.use_cases.upload_document import UploadDocumentUseCase
from infrastructure.repositories.local_document_repository import LocalDocumentRepository
from config.logging import setup_logging
from fastapi import FastAPI, UploadFile, File, HTTPException

from google import genai
from google.genai import types

logger = setup_logging()
app = FastAPI()
client = genai.Client(api_key=get_settings().GEMINI_API_KEY)

semantic_query_service = GeminiQueryServiceImpl(client)
document_repository = LocalDocumentRepository()


@app.get("/health")
def read_root():
    return {"health": "ok"}

@app.post(
        "/brief", 
        description="Endpoint for upload project documents")
def generate_brief(files: List[UploadFile] = File(...)):
    if not files:
        return {"error": "No files uploaded."}
    if not isinstance(files, list):
        files = [files]
    uploader = GeminiUploaderImpl(client)
    
    use_case = UploadDocumentUseCase(document_repository=document_repository, uploader=uploader, semantic_query_service=semantic_query_service)
    uploaded_documents = use_case.upload(files)
    
    return BriefResponse(
        project_id=uploaded_documents.document.project_id,
        brief=uploaded_documents.gemini_response.message
    )

@app.post("/search",
          responses={404: {"description": "Project not found"}},
          description="Endpoint for semantic search over project documents")
def run_search(query: SemanticQuery):
    try:
        use_case = SemanticQueryUseCase(
            semantic_query_service=semantic_query_service,
            repository=document_repository)
        
        response = use_case.execute(project_id=query.project_id, prompt=query.query)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Project not found.")
    return SearchResult(results=response)