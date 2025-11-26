from core.domain.entities import UploadResult

class UploadDocumentUseCase:
    def __init__(self, document_repository, uploader):
        self.document_repository = document_repository
        self.uploader = uploader

    def upload(self, files):
        for file in files:
            data: bytes = file.file.read()
            document = self.document_repository.save(data, file.filename)

            result = self.uploader.upload(document.path, document.filename)

        return UploadResult(
            gemini_response=result,
            document=document
        )