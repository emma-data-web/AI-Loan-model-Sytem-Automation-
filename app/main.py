from fastapi import FastAPI
from routes import auth_routes, loan_routes
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Loan System")

app.include_router(auth_routes.router)
app.include_router(loan_routes.router)
