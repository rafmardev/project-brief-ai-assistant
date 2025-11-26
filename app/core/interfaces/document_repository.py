from abc import ABC, abstractmethod

from core.domain.entities import Document

class DocumentRepository(ABC):
    @abstractmethod
    def save(self, documents: list, project_id: str) -> str:
        """Saves a document and returns its storage path."""
        pass
    @abstractmethod
    def get(self, project_id: str) -> list[Document]:
        """Retrieves if project_id is valid and its documents."""
        pass