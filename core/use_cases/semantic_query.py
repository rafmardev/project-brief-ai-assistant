
from core.domain.entities import Document, FileSearchResult


class SemanticQueryUseCase:
    def __init__(self, semantic_query_service, repository):
        self.semantic_query_service = semantic_query_service
        self.repository = repository

    def execute(self, project_id: str, prompt: str) -> list[Document]:
        documents = self.repository.get(project_id)
        response = []
        
        for document in documents:
            response.append(
                FileSearchResult(
                    file=document.filename, snippet=self.semantic_query_service.query(project_id, prompt)
                )
            )
        
        return response