from typing import List
from app.core.use_cases.upload_document import UploadDocumentUseCase
from app.infrastructure.repositories.local_document_repository import LocalDocumentRepository
from app.infrastructure.gemini.gemini_uploader_dummy import GeminiUploaderDummy
from config.logging import setup_logging
from fastapi import FastAPI, UploadFile, File

logger = setup_logging()
app = FastAPI()

@app.get("/health")
def read_root():
    return {"Hello": "World"}

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
    return {"message": "This endpoint will handle file uploads and generate a project brief."}

# Run semantic queries over the uploaded files
@app.post("/search")
def run_search():
    return {"message": "This endpoint will handle semantic queries over the uploaded files."}