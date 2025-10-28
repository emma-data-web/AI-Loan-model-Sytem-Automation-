from pydantic import BaseModel, EmailStr

class UserCreateRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "analyst"


class UserCreateResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserProfileResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str = "analyst"