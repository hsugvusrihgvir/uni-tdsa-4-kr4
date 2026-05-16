from pydantic import BaseModel, EmailStr, conint, constr
from typing import Optional


class CustomExceptionModel(BaseModel):
    status_code: int
    er_message: str
    er_details: str


class ItemResponse(BaseModel):
    id: int

class User(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = "Unknown"