import logging
from core.domain.entities import UploadResult

logger = logging.getLogger(__name__)
class UploadDocumentUseCase:
    def __init__(self, document_repository, uploader):
        self.document_repository = document_repository
        self.uploader = uploader

    def upload(self, files):
        project_id = self.uploader.create_store()
        for file in files:
            document = self.document_repository.save(file, project_id=project_id)
            self.uploader.upload(document.path, project_id)
            logger.info(f"Uploaded document {document.filename} to Gemini store {project_id}.")
        
        result = self.uploader.generate_brief(project_id)

        return UploadResult(
            gemini_response=result,
            document=document
        )