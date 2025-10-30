from models.loan_model import Loan
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

def create_loan(db: Session, user_id: int, amount: float, duration: int, purpose: str = None):
    new_loan = Loan(
        user_id=user_id,
        amount=amount,
        duration=duration,
        purpose=purpose,
        status="pending",
        timestamp=datetime.utcnow()
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

def get_user_loans(db: Session, user_id: int):
    return db.query(Loan).filter(Loan.user_id == user_id).all()
