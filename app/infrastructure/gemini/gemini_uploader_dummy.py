
import uuid
from core.domain.entities import GeminiResponse
from core.interfaces.gemini_uploader import GeminiUploader

class GeminiUploaderDummy(GeminiUploader):
    def create_store(self) -> str:
        # Dummy implementation for testing
        return f"{uuid.uuid4()}"
  
    def upload(self, file_path: str, store_id: str) -> str:
        # Dummy implementation for testing
        return f"file-{file_path}-in-store-{store_id}"
    
    def generate_brief(self, store_id: str) -> str:
            # Dummy implementation for testing
            return GeminiResponse(
                    message=f"This is a dummy brief summary for store {store_id}.",
                    success=True
                )