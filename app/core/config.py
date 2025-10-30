from pydantic_settings import BaseSettings
from fastapi.security import OAuth2PasswordBearer

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORIHMS : str
    ACESS_TOKEN_EXPIRATION: int

    class Config:
        env_file = ".env"


Settings = Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")