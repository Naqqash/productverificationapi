from pydantic import BaseModel
from fastapi import HTTPException


class VerificationResponseSchema(BaseModel):
    status_code: int
    status: bool = False
    detail: str
