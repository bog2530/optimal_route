from os import environ

from pydantic_settings import BaseSettings


class DefaultSettings(BaseSettings):
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/api")

    POSTGRES_USER: str = environ.get("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "12345")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = environ.get("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = "postgres"

    CORS_ALLOWED_ORIGINS: list = ["*"]

    def get_db_connection_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
