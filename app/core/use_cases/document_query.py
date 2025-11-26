
from core.domain.entities import Document, FileSearchResult


class QueryDocumentUseCase:
    def __init__(self, document_query_service, repository):
        self.document_query_service = document_query_service
        self.repository = repository

    def execute(self, project_id: str, prompt: str) -> list[Document]:
        documents = self.repository.get(project_id)
        response = []
        
        for document in documents:
            response.append(
                FileSearchResult(
                    file=document.filename, snippet=self.document_query_service.query(project_id, prompt)
                )
            )
        
        return response