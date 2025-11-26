from abc import ABC, abstractmethod

from core.domain.entities import Document

class DocumentRepository(ABC):
    @abstractmethod
    def save(self, documents: list) -> str:
        """Saves a document and returns its storage path."""
        pass
    @abstractmethod
    def get(self, project_id: str) -> list[bytes]:
        """Retrieves documents by its project_id."""
        pass