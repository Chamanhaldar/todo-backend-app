from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    DATABASE_URL: str = "sqlite:///./todo.db"
    API_V1_STR: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        
settings = Settings()