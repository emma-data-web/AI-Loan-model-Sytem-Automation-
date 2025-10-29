from sqlalchemy.orm import Session
from  fastapi import HTTPException
from models.user_model import User
from schemas.user_schema import UserCreateRequest, UserLoginRequest, UserProfileResponse
from utils.password_utils import hash_password, verify_password
from utils.jwt_handler import create_access_token



def register_user(db: Session, user: UserLoginRequest):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="username already taken")
    hashed_pw = hash_password(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw,
        role = user.role

    )
    db.add(new_user)
    db.commit()
    return new_user


def login_user(db: Session, user: UserLoginRequest):
    db_user = db.query(User).filter(User.username == user.username)
    if not db_user or not verify_password(user.password, db_user.hash_password):
        raise HTTPException(status_code=401, detail="invalid username or password")
    access_token = create_access_token({"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

