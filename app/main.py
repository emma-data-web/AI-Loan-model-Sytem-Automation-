from fastapi import FastAPI

app = FastAPI(title="AI LOAN MODEL AND SYSTEM MONITORING")

@app.get("/")
def home():
    return {"message": "welcome home"}