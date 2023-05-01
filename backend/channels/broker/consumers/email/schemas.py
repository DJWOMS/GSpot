from pydantic import BaseModel


class Mail(BaseModel):
    uuid: int
    email: str
    subject: str
    body: str
