from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Notification(BaseModel):
    """ Notification model """
    id: Optional[ObjectId] = Field(alias="_id")
    user_id: ObjectId = Field(...)
    text: str = Field(...)
    status: str = Field(default="unread")
    timestamp: datetime = Field(default=datetime.utcnow())
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