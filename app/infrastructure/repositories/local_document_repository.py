from logging import config
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