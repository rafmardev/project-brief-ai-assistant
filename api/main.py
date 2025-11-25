from typing import List
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
    return {"message": "This endpoint will handle file uploads and generate a project brief."}

# Run semantic queries over the uploaded files
@app.post("/search")
def run_search():
    return {"message": "This endpoint will handle semantic queries over the uploaded files."}