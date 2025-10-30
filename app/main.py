from fastapi import FastAPI
from routes.auth.routes_auth import router as auth_routes
from routes.loan.routes_loan import router as  loan_routes
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Loan System")

app.include_router(auth_routes)
app.include_router(loan_routes)
