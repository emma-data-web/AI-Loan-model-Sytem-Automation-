import time
import pandas as pd
from sqlalchemy.orm import Session
from app.core.database import get_db
from services.loan_service import predict_risk  
from models.loan_model import Loan
import joblib
import logging


model = joblib.load("ml_models/loan_model.pkl")


logging.basicConfig(
    filename="loan_prediction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_loop():
    logging.info("Starting background loan prediction loop")
    
    while True:
        db: Session = next(get_db())
        
        
        new_loans = db.query(Loan).filter(Loan.risk_score == None).all()
        if new_loans:
            logging.info(f"Found {len(new_loans)} new loans to predict")
            for loan in new_loans:
                
                df = pd.DataFrame([{
                    "amount": loan.amount,
                    "duration": loan.duration,
                    "income": 0,  
                    "credit_score": 0, 
                    "purpose": loan.purpose
                }])
                
                # Predict
                risk = predict_risk(model, df)
                loan.risk_score = float(risk[0])
                db.commit()
                logging.info(f"Predicted risk {risk[0]} for loan id {loan.id}")
        
        else:
            logging.info("No new loans to predict")
        
        time.sleep(60)  

if __name__ == "__main__":
    run_loop()
