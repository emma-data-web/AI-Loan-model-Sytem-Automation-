from sqlalchemy import Column, Integer,  String, Float
from app.core.database import Base


class UserLoan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, index=True)
    applicant = Column(String)
    amount = Column(Float)
    income = Column(Float)
    credit_score = Column(Float)
    status = Column(String, default="pending")
    risk_score = Column(Float, default=None)
