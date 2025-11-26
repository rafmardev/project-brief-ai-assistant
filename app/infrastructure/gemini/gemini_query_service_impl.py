
from core.domain.entities import GeminiResponse
from core.interfaces.gemini_query_service import GeminiQueryService
from google.genai import types

class GeminiQueryServiceImpl(GeminiQueryService):
    def __init__(self, api_client):
        self.api_client = api_client
        
    def query(self, store_id: str, prompt: str) -> str:
        # Ask a question about the file
        response = self.api_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[f"fileSearchStores/{store_id}"]
                        )
                    )
                ]
            )
        )
        
        return GeminiResponse(
                message=response.text,
                success=True
        )