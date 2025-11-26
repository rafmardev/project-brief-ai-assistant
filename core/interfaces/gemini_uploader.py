from abc import ABC, abstractmethod

class GeminiUploader(ABC):
    @abstractmethod
    def create_store(self, file_path: str, store_id: str) -> str:
        """Uploads a file to Gemini and returns the file URL."""
        pass
    
    @abstractmethod
    def upload(self, file_path: str, store_id: str) -> str:
        """Uploads a file to Gemini and returns the file URL."""
        pass