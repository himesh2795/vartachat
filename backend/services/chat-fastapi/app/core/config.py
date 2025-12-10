from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import List
from pydantic import Field, BaseModel


class DatabaseSettings(BaseModel):
    """Database related settings."""
    URL: str = Field(default="sqlite:///./chat.db", description="Database connection URL")
    POOL_SIZE: int = Field(default=5, description="Database connection pool size")
    MAX_OVERFLOW: int = Field(default=10, description="Database max overflow")

    @property
    def sqlalchemy_database_url(self) -> str:
        """Get SQLAlchemy database URL."""
        return self.URL


class SecuritySettings(BaseModel):
    """Security related settings."""
    ALLOWED_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        description="List of allowed origins for CORS"
    )


class JWTSettings(BaseModel):
    """JWT authentication settings."""
    SECRET_KEY: str = Field(..., description="Secret key for JWT token generation")
    ALGORITHM: str = Field(default="HS256", description="Algorithm for JWT")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiry in minutes")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, description="Refresh token expiry in days")


class ApplicationSettings(BaseSettings):
    """Main application settings that combines all other settings."""
    PROJECT_NAME: str = "Chat FastAPI"
    ENVIRONMENT: str = Field(default="dev", description="Current environment (dev/stage/prod)")
    DEBUG: bool = Field(default=True, description="Debug mode")
    API_V1_STR: str = "/api/v1"

    # Nested settings
    db: DatabaseSettings
    jwt: JWTSettings
    security: SecuritySettings

    model_config = SettingsConfigDict(
        env_file=".env" if __import__("os").getenv("ENVIRONMENT") == "prod" else ".env.local",
        env_nested_delimiter="__",
        extra="ignore",
        case_sensitive=True
    )

    @property
    def is_production(self) -> bool:
        """Check if the application is running in production."""
        return self.ENVIRONMENT == "prod"


@lru_cache()
def get_settings() -> ApplicationSettings:
    """
    Get application settings, cached for better performance.
    """
    return ApplicationSettings()


# Global settings instance
settings = get_settings()
