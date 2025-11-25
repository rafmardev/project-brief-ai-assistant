from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API general
    APP_NAME: str = "Document API"
    ENV: str = "development"

    # Gemini
    GEMINI_ENDPOINT: str
    GEMINI_API_KEY: str

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_GROUP_ID: str = "document-events"
    KAFKA_TOPIC_DOCUMENT_UPLOADED: str = "document.uploaded"

    # Storage
    STORAGE_PATH: str = "../infrastructure/storage"

    class Config:
        env_file = ".env"   # Permite cargar credenciales desde .env

@lru_cache()
def get_settings():
    return Settings()
