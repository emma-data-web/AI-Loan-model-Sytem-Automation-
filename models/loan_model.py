from sqlalchemy import Column, Integer,  String, Float
from app.core.database import Base


class UserLoan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, index=True)
    applicant_name = Column(String, nullable=False)
    applicant_income = Column(Float, nullable=False)
    applicant_amount = Column(Float, nullable=False)
    loan_amount = Column(Float, nullable=False)
    loan_term = Column(Float, nullable=False)
    credit_score = Column(Float, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    employment_status = Column(String, nullable=False)
    purpose = Column(String, nullable=False)
    status = Column(String, default="pending")
    prediction_score = Column(Float, nullable=True)
