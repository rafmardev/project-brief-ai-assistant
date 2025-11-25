from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API general
    APP_NAME: str = "Document API"
    ENV: str = "development"

    # Gemini
    GEMINI_ENDPOINT: str
    GEMINI_API_KEY: str

    # Storage
    STORAGE_PATH: str = "../infrastructure/storage"

    class Config:
        env_file = "./config/.env"

@lru_cache()
def get_settings():
    return Settings()
