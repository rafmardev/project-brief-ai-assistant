
from core.domain.entities import GeminiResponse
from core.interfaces.gemini_uploader import GeminiUploader

class GeminiUploaderDummy(GeminiUploader):
    def upload(self, file_path: str, display_name: str) -> str:
        # Dummy implementation for testing
        return GeminiResponse(
                message=f"This is a dummy upload response from GeminiUploaderDummy of {display_name} in {file_path}.",
                success=True
            )