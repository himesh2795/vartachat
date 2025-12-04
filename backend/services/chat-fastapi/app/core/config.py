from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Chat FastAPI"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    
    class Config:
        case_sensitive = True

settings = Settings()
