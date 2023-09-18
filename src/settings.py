from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    # Environment
    DEBUG: bool = False
    LOG_LEVEL: str = "ERROR"
    GUNICORN_WORKERS: int = 3
    ENVIRONMENT: str = "local"
    APPLICATION_PORT: int = 8011
    BASE_PATH: str = "/cinefy"
    BASE_DIR: Path = Path(__file__).resolve(strict=True).parent.parent
    CORS_ORIGINS: str = "*"

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = "5432"
    DB_NAME: str = "test_db"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "cantguessthis"

    # Sentry
    DSN: str = "https://3e440eb7914699735b72303583e067b4@o4505902962180096.ingest.sentry.io/4505902964736000"


settings = Settings()
