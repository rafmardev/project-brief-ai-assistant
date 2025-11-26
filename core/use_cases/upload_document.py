import logging
from core.domain.entities import UploadResult

logger = logging.getLogger(__name__)
class UploadDocumentUseCase:
    def __init__(self, document_repository, uploader, semantic_query_service):
        self.document_repository = document_repository
        self.uploader = uploader
        self.semantic_query_service = semantic_query_service

    def upload(self, files):
        project_id = self.uploader.create_store()
        for file in files:
            document = self.document_repository.save(file, project_id=project_id)
            self.uploader.upload(document.path, project_id)
        
        result = self.semantic_query_service.query(project_id, "Do a brief summary of the contents all the files of the store.")

        return UploadResult(
            gemini_response=result,
            document=document
        )