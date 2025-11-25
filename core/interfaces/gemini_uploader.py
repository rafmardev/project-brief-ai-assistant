from abc import ABC, abstractmethod

class GeminiUploader(ABC):
    @abstractmethod
    def upload(self, file_path: str, display_name: str) -> str:
        """Uploads a file to Gemini and returns the file URL."""
        pass