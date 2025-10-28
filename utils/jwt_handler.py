from datetime import datetime, timedelta
from jose import JWTError, jwt 
from app.core.config import Settings


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Settings.ACESS_TOKEN_EXPIRATION)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings.SECRET_KEY,algorithm=Settings.ALGORIHMS)
    return encoded_jwt