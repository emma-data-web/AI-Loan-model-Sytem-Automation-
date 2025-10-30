from fastapi import FastAPI
from app.core.database import Base, engine

from models.user_model import User
from models.loan_model import Loan


from routes.auth.routes_auth import router as auth_routes
from routes.loan.routes_loan import router as loan_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Loan System")


app.include_router(auth_routes)
app.include_router(loan_routes)
