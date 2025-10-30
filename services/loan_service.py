import joblib
from sqlalchemy.orm import Session
from models.loan_model import Loan  
import pandas as pd
import numpy as np


model = joblib.load("loan_model.pkl")

def create_loan(db: Session, user_id: int, amount: float, duration: int, purpose: str):
    
    input_df = pd.DataFrame([{
        "amount": amount,
        "duration": duration,
        "income": 0,        
        "credit_score": 0,  
        "purpose": purpose
    }])

    
    risk_score = float(model.predict_proba(input_df)[:,1][0])
    
    
    prediction = int(model.predict(input_df)[0])

    
    new_loan = Loan(
        user_id=user_id,
        amount=amount,
        duration=duration,
        purpose=purpose,
        risk_score=risk_score,
        status="pending"
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    
    return new_loan

def get_user_loans(db: Session, user_id: int):
    return db.query(Loan).filter(Loan.user_id == user_id).all()
