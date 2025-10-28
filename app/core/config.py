from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORIHMS : str
    ACESS_TOKEN_EXPIRATION: int

    class Config:
        env_file = ".env"


Settings = Settings()

