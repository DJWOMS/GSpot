from pydantic import BaseModel


class NotificationResponse(BaseModel):
    code: str
    status: str
    message: str
    result: list
