from sqlalchemy.orm import Session
from  fastapi import HTTPException
from models.loan_model import UserLoan
from schemas.loan_schema import LoanRequest


#create new loan

def create_loan(db: Session, loan_data: LoanRequest):
    new_loan = UserLoan(
       applicant_name = loan_data.applicant_name,
       amount = loan_data.amount,
       income = loan_data.income,
       credit_score = loan_data.credit_score,
       status = "pending",
       risk_score = None
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

# get all loans

def get_all_loan(db: Session):
    return db.query(UserLoan).all()

# get one
def get_single_loan_by_id(db: Session, loan_id: int):
    return db.query(UserLoan).filter(UserLoan.id == loan_id).first()

