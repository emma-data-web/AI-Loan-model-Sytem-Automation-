from fastapi import FastAPI
from app.core.database import Base, engine

from app.models.user_model import User
from app.models.loan_model import Loan


from app.routes.auth.routes_auth import router as auth_routes
from app.routes.loan.routes_loan import router as loan_routes




app = FastAPI(title="AI Loan System")


app.include_router(auth_routes)
app.include_router(loan_routes)


