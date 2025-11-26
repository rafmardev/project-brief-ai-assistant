from logging import config
import os
import uuid
from config.settings import get_settings
from core.domain.entities import Document, DocumentFile;
from core.interfaces.document_repository import DocumentRepository;

class LocalDocumentRepository(DocumentRepository):
    def save(self, document: bytes, project_id: str) -> str:
        """Saves a documents locally in a project_id folder and returns its storage path."""
        path = f"{get_settings().STORAGE_PATH}/{project_id}/"

        if not os.path.exists(path):
            os.makedirs(path)
        full_path = os.path.join(path, document.filename)
        with open(full_path, 'wb') as f:
            f.write(document.file.read())

        return Document(project_id, document.filename, full_path)
    
    def get(self, project_id: str) -> list[bytes]:
        """Retrieves documents by its project_id."""
        documents = []
        path = None
        if not os.path.exists(f"{get_settings().STORAGE_PATH}/{project_id}"):
            raise FileNotFoundError(f"Project with ID {project_id} not found.")

        for path, _, files in os.walk(f"{get_settings().STORAGE_PATH}/{project_id}"):
            for file_name in files:
                full_path = os.path.join(path, file_name)
                documents.append(
                        Document(project_id, file_name, full_path)                       
                    )
                    
        
        return documents