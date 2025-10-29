from sqlalchemy import Column, Integer,  String
from app.core.database import Base


class User(Base):
    __table__name = "loan"

    id = Column(Integer, primary_key=True, index=True)
    applicant = Column(String)
    amount = Column(float)
    income = Column(float)
    credit_score = Column(float)
    status = Column(String, default="pending")
    risk_score = Column(float, default=None)
    