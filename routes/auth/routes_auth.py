from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.user_schema import UserCreateRequest, UserCreateResponse, UserLoginRequest
from services.auth_service import register_user, login_user


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserCreateResponse)
def register(user: UserCreateRequest, db: Session =Depends(get_db)):
    return register_user(db,user)

@router.post("/login")
def login(user: UserLoginRequest, db: Session= Depends(get_db)):
    return login_user
