from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoanCreateRequest(BaseModel):
    amount: float
    duration: int
    purpose: Optional[str] = None

class LoanResponse(BaseModel):
    id: int
    amount: float
    duration: int
    purpose: Optional[str]
    status: str
    risk_score: Optional[float]
    timestamp: datetime

    class Config:
        orm_mode = True
