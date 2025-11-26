from core.domain.entities import GeminiResponse
from core.interfaces.gemini_uploader import GeminiUploader
# Google API
from google import genai
from google.genai import types
import time
import logging
logger = logging.getLogger(__name__)

class GeminiUploaderImpl(GeminiUploader):
    def __init__(self, api_client):
        self.api_client = api_client

    def create_store(self) -> str:
        # Create the File Search store
        file_search_store = self.api_client.file_search_stores.create()
        logger.info(f"Created Gemini File Search store with name: {file_search_store}")
        prefix = "fileSearchStores/"
        if file_search_store.name.startswith(prefix):
            file_search_store.name = file_search_store.name[len(prefix):]
        return file_search_store.name

    def upload(self, file_path: str, store_id: str) -> str:
        # Upload and import a file into the File Search store, supply a file name which will be visible in citations
        operation = self.api_client.file_search_stores.upload_to_file_search_store(
        file=file_path,
        file_search_store_name=f"fileSearchStores/{store_id}"
        )

        # Wait until import is complete
        while not operation.done:
            time.sleep(5)
            operation = self.api_client.operations.get(operation)

    def generate_brief(self, store_id):
        # Ask a question about the file
        response = self.api_client.models.generate_content(
            model="gemini-2.5-flash",
            contents="""Do a brief summary of the contents all the files of the store.""",
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