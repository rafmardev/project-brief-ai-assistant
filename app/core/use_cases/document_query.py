
from http.client import HTTPException

from core.domain.entities import FileSearchResult


class QueryDocumentUseCase:
    def __init__(self, document_query_service, repository):
        self.document_query_service = document_query_service
        self.repository = repository

    def execute(self, project_id: str, prompt: str) -> list[FileSearchResult]:
        files = self.repository.get(project_id)
        response = []
        
        for document_file in files:
            response.append(
                FileSearchResult(file=document_file.document.filename, snippet=self.document_query_service.query(document_file.file, prompt)
                                 )
            )
        
        return response