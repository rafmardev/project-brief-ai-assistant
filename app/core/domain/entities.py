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

@dataclass
class BriefResponse:
    project_id: str
    brief: str

@dataclass
class SemanticQuery:
    project_id: str
    query: str

@dataclass
class FileSearchResult:
    file: str
    snippet: str

@dataclass
class SearchResult:
    results: list[FileSearchResult]