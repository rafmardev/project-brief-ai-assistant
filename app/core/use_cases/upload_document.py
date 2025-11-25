from app.core.domain.entities import UploadResult

class UploadDocumentUseCase:
    def __init__(self, document_repository, uploader):
        self.document_repository = document_repository
        self.uploader = uploader

    def upload(self, files):
        for file in files:
            content = file.file.read()
            document = self.document_repository.save(file.filename, content)

            result = self.uploader.upload(document)

        return UploadResult(
            gemini_response=result,
            document=document
        )