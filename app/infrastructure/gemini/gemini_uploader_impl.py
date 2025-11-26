from app.core.domain.entities import GeminiResponse
from core.interfaces.gemini_uploader import GeminiUploader
# Google API
from google import genai
from google.genai import types
import time

class GeminiUploaderImplementation(GeminiUploader):
     def upload(self, file_path: str, display_name: str) -> str:
         # Implementation for uploading a file to Gemini
         
        client = genai.Client()

        # Upload the file using the Files API, supply a file name which will be visible in citations
        sample_file = client.files.upload(file=file_path, config={'name': display_name})

        # Create the File Search store with an optional display name
        file_search_store = client.file_search_stores.create(config={'display_name': display_name})

        # Import the file into the File Search store
        operation = client.file_search_stores.import_file(
            file_search_store_name=file_search_store.name,
            file_name=sample_file.name
        )

        # Wait until import is complete
        while not operation.done:
            time.sleep(5)
            operation = client.operations.get(operation)

        # Ask a question about the file
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="""Do a brief summary of the contents of the file.""",
            config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ]
            )
        )

        return GeminiResponse(
                message=response.content,
                success=True
            )