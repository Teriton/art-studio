from pydantic import BaseModel
from database import modelsDTO

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: str | None = None


class PaymentMethodModel(BaseModel):
    payment_method: modelsDTO.PaymentMethod
    