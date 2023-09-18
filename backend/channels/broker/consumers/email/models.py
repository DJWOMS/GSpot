import uuid

from pydantic import BaseModel, EmailStr


class Mail(BaseModel):
    uuid: uuid.UUID
    email: EmailStr
    subject: str
    body: str
