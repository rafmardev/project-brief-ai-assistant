from core.domain.entities import UploadResult

class UploadDocumentUseCase:
    def __init__(self, document_repository, uploader):
        self.document_repository = document_repository
        self.uploader = uploader

    def upload(self, files):        
        document = self.document_repository.save(files)

        result = self.uploader.upload(document.path, document.filename)

        return UploadResult(
            gemini_response=result,
            document=document
        )