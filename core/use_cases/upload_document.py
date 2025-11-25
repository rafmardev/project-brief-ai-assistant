class UploadDocumentUseCase:
    def __init__(self, document_repository, event_bus):
        self.document_repository = document_repository
        self.event_bus = event_bus

    def upload(self, files):
        uploaded_files = []
        for file in files:
            content = file.file.read()
            document = self.document_repository.save(file.filename, content)

            self.event_bus.publish(
                "document_uploaded", {
                    "id": document.id,
                    "filename": file.filename,
                    "path": document.path
            })
        return uploaded_files