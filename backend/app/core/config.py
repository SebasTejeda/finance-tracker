from pydantic_settings import BaseSettings
from typing import List
import json


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # CORS - Convertir string JSON a lista
    CORS_ORIGINS: str = '["http://localhost:4200"]'

    @property
    def cors_origins_list(self) -> List[str]:
        """Convertir el string JSON de CORS_ORIGINS a lista"""
        return json.loads(self.CORS_ORIGINS)

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
