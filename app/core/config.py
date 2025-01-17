import os
from functools import lru_cache
from pathlib import Path
from typing import Optional, Union

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """Settings Class."""

    PROJECT_NAME: Optional[str] = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: Optional[str] = os.getenv("PROJECT_VERSION", "1.0.0")
    DB_USER: Optional[str] = os.getenv("DB_USER")
    DB_PASSWORD: Optional[str] = os.getenv("DB_PASSWORD")
    DB_HOST: Optional[str] = os.getenv("DB_HOST", "localhost")
    DB_PORT: Union[str, int, None] = os.getenv("DB_PORT", 3306)
    DB_NAME: Optional[str] = os.getenv("DB_NAME", "tdd")
    ENVIRONMENT: Optional[str] = os.getenv("ENVIRONMENT", "test")
    DATABASE_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = os.getenv("SECRET_KEY", "somesecretkey")


@lru_cache
def get_settings() -> Settings:
    """Get cached settings."""
    settings = Settings()
    return settings
