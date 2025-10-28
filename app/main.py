from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import Base, engine, get_db
from routes.auth.routes_auth import routes_auth



app = FastAPI(title="AI LOAN MODEL AND SYSTEM MONITORING")

Base.metadata.create_all(bind=engine)

app.include_router(routes_auth.router)

@app.get("/")
def home(db: Session= Depends(get_db)):
    return {"message": "welcome home"}