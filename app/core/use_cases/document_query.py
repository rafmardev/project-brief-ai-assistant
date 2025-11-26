
from http.client import HTTPException


class QueryDocumentUseCase:
    def __init__(self, document_query_service, repository):
        self.document_query_service = document_query_service
        self.repository = repository

    def execute(self, file_id: str, prompt: str) -> str:
        file_bytes = self.repository.get(file_id)
        response = self.document_query_service.query(file_bytes, prompt)
        return response