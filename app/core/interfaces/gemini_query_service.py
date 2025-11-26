from core.domain.entities import Document
from abc import ABC, abstractmethod

class GeminiQueryService(ABC):
    @abstractmethod 
    def query(self, file_bytes: bytes, prompt: str) -> str:
        """Retrieves a document by its ID."""
        pass    