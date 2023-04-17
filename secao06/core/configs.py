from typing import List 
from pydantic import BaseSettings   
from  sqlalchemy.ext.declarative import declarative_base    



class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
    DBBaseModel = declarative_base()
    """
    terminal > python > import secrets > token: str = secrets.token_urlsafe(32)  >  token > ex: M-tjOP8YLH82nBQRJEZxRMFK2VD4-1Qi5PQ25FlRHr4
    """
    JWT_SECRET: str = 'M-tjOP8YLH82nBQRJEZxRMFK2VD4-1Qi5PQ25FlRHr4' #TOKEN GERADO PELA BIBLIOTECA
    
    ALGORITHM: str = 'HS252'
    # uma semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
        
        
settings: Settings = Settings()        