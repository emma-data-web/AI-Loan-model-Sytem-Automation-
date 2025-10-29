from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.loan_schema import LoanRequest, LoanResponse
from services.loan_service import create_loan, get_all_loan, get_single_loan_by_id


router = APIRouter(prefix="/loan", tags=["LOAN"])

@router.post("/apply", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def apply_loan(loan_data: LoanRequest, db: Session= Depends(get_db)):
    new_loan = create_loan(db, loan_data)
    return new_loan

@router.get("/all", response_model=list[LoanResponse])
def list_loan(db: Session = Depends(get_db)):
    loans = get_all_loan(db)
    return loans

@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan_by_id(loan_id: int, db:Session = Depends(get_db)):
    loan = get_single_loan_by_id(db, loan_id)
    if not loan:
        raise HTTPException("user or applicant does not exist")
    return loan