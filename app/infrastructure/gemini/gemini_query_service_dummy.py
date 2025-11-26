
from core.interfaces.gemini_query_service import GeminiQueryService
from core.domain.entities import GeminiResponse

class GeminiQueryServiceDummy(GeminiQueryService):
    def query(self, file_bytes: bytes, prompt: str) -> str:
        # Dummy implementation for testing
        return GeminiResponse(
                message=f"This is a dummy query response from GeminiQueryServiceDummy for prompt: {prompt}.",
                success=True
            )