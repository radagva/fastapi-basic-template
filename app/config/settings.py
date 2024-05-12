from pydantic_settings import BaseSettings
from os import environ
from functools import lru_cache
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    APP_NAME: str = environ.get("APP_NAME", "App name")
    DEBUG: str | bool = environ.get("DEBUG", False)

    DATABASE_ENGINE: str = environ.get("DATABASE_ENGINE", "postgresql")
    DATABASE_HOST: str = environ.get("DATABASE_HOST", "localhost")
    DATABASE_PORT: str = environ.get("DATABASE_PORT", "5432")
    DATABASE_NAME: str = environ.get("DATABASE_NAME", "root")
    DATABASE_USER: str = environ.get("DATABASE_USER", "root")
    DATABASE_PASSWORD: str = environ.get("DATABASE_PASSWORD", "123456")
    DATABASE_URI: str = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    ALGORITHM: str = environ.get("ALGORITHM", "RANDOM_ALGORITHM")
    SECRET_KEY: str = environ.get("SECRET_KEY", "SOME_KEY")


@lru_cache()
def get_settings():
    return Settings()
