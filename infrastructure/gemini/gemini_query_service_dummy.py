
from core.interfaces.gemini_query_service import GeminiQueryService
from core.domain.entities import GeminiResponse

class GeminiQueryServiceDummy(GeminiQueryService):
    def query(self, store_id: str, prompt: str) -> str:
        # Dummy implementation for testing
        return GeminiResponse(
                message=f"This is a dummy query response from GeminiQueryServiceDummy for prompt: {prompt} of {store_id}.",
                success=True
            )