
from app.core.domain.entities import GeminiResponse
from core.interfaces.gemini_query_service import DocumentQueryService


class GeminiQueryServiceImpl(DocumentQueryService):
    def __init__(self, api_client):
        self.api_client = api_client
        
    def query(self, file_bytes: bytes, prompt: str) -> str:
        response = self.api_client.query_document(file_bytes, prompt)
        return GeminiResponse(
                message=response.content,
                success=True
            )