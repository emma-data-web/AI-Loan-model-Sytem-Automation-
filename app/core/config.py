from pydantic_settings import BaseSettings
from fastapi.security import OAuth2PasswordBearer

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORIHMS : str
    ACCESS_TOKEN_EXPIRATION: int

    class Config:
        env_file = ".env"


settings = Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")