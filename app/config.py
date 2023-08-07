from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "FastAPI Sandbox"
    APP_DESCRIPTION: str = "FastAPI Sandbox"
    APP_VERSION: str = "0.0.1"

    # Database
    DATABASE_DRIVER: str = "postgresql"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "fastapi_sandbox"
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    # CORS
    ALLOWED_CORS_ORIGIN: set[AnyUrl] = set("")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
