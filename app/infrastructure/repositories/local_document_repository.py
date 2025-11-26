from logging import config
import os
import uuid
from config.settings import get_settings
from core.domain.entities import Document;
from core.interfaces.document_repository import DocumentRepository;

class LocalDocumentRepository(DocumentRepository):
    def save(self, documents: list) -> str:
        """Saves a documents locally in a project_id folder and returns its storage path."""
        project_id = f"{uuid.uuid4()}"
        path = f"{get_settings().STORAGE_PATH}/{project_id}/"

        for document in documents:
            if not os.path.exists(path):
                os.makedirs(path)
            full_path = os.path.join(path, document.filename)
            with open(full_path, 'wb') as f:
                f.write(document.file.read())
                
        return Document(project_id, document.filename, path)
    
    def get(self, project_id: str) -> list[bytes]:
        """Retrieves documents by its project_id."""
        document_bytes = []
        path = None
        for root, _, files in os.walk(get_settings().STORAGE_PATH):
            for filename in files:
                if project_id in filename:
                    path = os.path.join(root, filename)
                    break

        if not path:
            raise FileNotFoundError(f"Document with ID {project_id} not found.")

        for path, _, files in os.walk(f"{get_settings().STORAGE_PATH}/{project_id}"):
            for filename in files:
                with open(path, 'rb') as file:
                    document_bytes.append(file.read())
        
        return document_bytes