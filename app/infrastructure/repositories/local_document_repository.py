import uuid
from core.domain import Document;
from core.interfaces.document_repository import DocumentRepository;

class LocalDocumentRepository(DocumentRepository):
    def save(self, document: bytes, filename: str) -> str:
        """Saves a document locally and returns its storage path."""
        uuid_filename = f"{uuid.uuid4()}_{filename}"
        path = f"./storage/{uuid_filename}"
        with open(path, 'wb') as f:
            f.write(document)
        return Document(uuid_filename, filename, path)