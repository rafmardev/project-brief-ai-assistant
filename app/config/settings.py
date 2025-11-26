import os
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
    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STORAGE_FOLDER: str = "infrastructure/storage"
    STORAGE_PATH: str = os.path.join(PROJECT_ROOT, STORAGE_FOLDER)

    class Config:
        env_file = "./config/.env"

@lru_cache()
def get_settings():
    return Settings()
