from dataclasses import dataclass
@dataclass
class Document:
    id: str
    filename: str
    path: str

@dataclass
class GeminiResponse:
    message: str
    success: bool

@dataclass
class UploadResult:
    gemini_response: GeminiResponse
    document: Document