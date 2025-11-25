class NotifyGeminiUseCase:
    def __init__(self, gemini_client):
        self.gemini_client = gemini_client

    def notify(self, message):
        self.gemini_client.send(
            message["path"],
            message["filename"]
        )