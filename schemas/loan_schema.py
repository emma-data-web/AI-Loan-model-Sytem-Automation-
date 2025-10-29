from pydantic import BaseModel

class LoanRequest(BaseModel):
    applicant : str
    amount : float
    income : float
    credit_score : float


class LoanResponse(BaseModel):
    id : int
    appilicant : str
    amount : float
    income : float
    credit_score : float
    status : str
    risk_score : float

    class Config:
        orm_mode = True


    