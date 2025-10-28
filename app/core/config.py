from pydantic import BaseSettings 

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORIHMS : str
    ACESS_TOKEN_EXPIRATION: int

    class config:
        env_file = ".env"


Settings = Settings()


"""
from app.core.config import settings 
print(settings.DATABASE_URL) --- a case example
"""