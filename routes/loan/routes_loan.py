from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.loan_schema import LoanCreateRequest, LoanResponse
from services.loan_service import create_loan, get_user_loans
from app.dependencies import get_current_user  

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", response_model=LoanResponse)
def apply_for_loan(request: LoanCreateRequest, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return create_loan(db, user["id"], request.amount, request.duration, request.purpose)

@router.get("/", response_model=list[LoanResponse])
def list_loans(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return get_user_loans(db, user["id"])
