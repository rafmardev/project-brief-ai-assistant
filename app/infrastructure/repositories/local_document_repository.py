from logging import config
import os
import uuid
from config.settings import get_settings
from core.domain.entities import Document;
from core.interfaces.document_repository import DocumentRepository;

class LocalDocumentRepository(DocumentRepository):
    def save(self, document: bytes, filename: str) -> str:
        """Saves a document locally and returns its storage path."""
        uuid_filename = f"{uuid.uuid4()}_{filename}"
        path = f"{get_settings().STORAGE_PATH}/{uuid_filename}"
        with open(path, 'wb') as f:
            f.write(document)
        return Document(uuid_filename, filename, path)
    
    def get(self, document_id: str) -> Document:
        """Retrieves a document by its ID."""
        path = None     
        for root, _, files in os.walk(get_settings().STORAGE_PATH):
            for filename in files:
                if document_id in filename:
                    path = os.path.join(root, filename)
                    break

        if not path:
            raise FileNotFoundError(f"Document with ID {document_id} not found.")

        with open(path, 'rb') as file:
            file_bytes = file.read()
        
        return file_bytes