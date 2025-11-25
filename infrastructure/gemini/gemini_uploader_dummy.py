
from core.interfaces.gemini_uploader import GeminiUploader

class GeminiUploaderDummy(GeminiUploader):
    def upload(self, file_path: str, display_name: str) -> str:
        # Dummy implementation for testing
        return "This is a dummy upload response from GeminiUploaderDummy."