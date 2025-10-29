from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import Base, engine, get_db
from routes.auth import routes_auth
from routes.auth.routes_auth import router as auth_router
from routes.loan.routes_loan import router as loan_router


app = FastAPI(title="AI LOAN MODEL AND SYSTEM MONITORING")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth")

app.include_router(loan_router, prefix="/loan")

@app.get("/")
def home(db: Session= Depends(get_db)):
    return {"message": "welcome home"}