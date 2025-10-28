from sqlalchemy import Column, Integer,  String
from app.core.database import Base


class User(Base):
    __tablename__ = "loanusers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="analyst")