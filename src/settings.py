from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    # Environment
    DEBUG: bool = False
    LOG_LEVEL: str = "ERROR"
    ENVIRONMENT: str
    APPLICATION_PORT: int
    BASE_PATH: str
    BASE_DIR: Path = Path(__file__).resolve(strict=True).parent.parent
    CORS_ORIGINS: str
    GUNICORN_WORKERS: int

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    # Sentry
    SENTRY_DSN: str = ""


settings = Settings()
