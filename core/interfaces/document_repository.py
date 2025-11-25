from abc import ABC, abstractmethod

class DocumentRepository(ABC):
    @abstractmethod
    def save(self, document: bytes, filename: str) -> str:
        """Saves a document and returns its storage path."""
        pass