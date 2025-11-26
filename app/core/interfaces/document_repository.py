from abc import ABC, abstractmethod

from core.domain.entities import Document

class DocumentRepository(ABC):
    @abstractmethod
    def save(self, document: bytes, filename: str) -> str:
        """Saves a document and returns its storage path."""
        pass
    @abstractmethod
    def get(self, document_id: str) -> bytes:
        """Retrieves a document by its ID."""
        pass