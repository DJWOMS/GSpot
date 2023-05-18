from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from utils.models import PydanticObjectId


class Notification(BaseModel):
    """ Notification model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    user_id: PydanticObjectId
    text: str
    status: str = Field(default="unread")
    created_at: datetime = Field(default=datetime.utcnow())
    timestamp_2: datetime = Field(default=datetime.utcnow())

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "user_id": "6148ed23aa02a1a38bde5e5d",
                "text": "You have a new message",
                "status": "unread",
                "timestamp": "2023-04-22T12:00:00.000Z"
            }
        }
