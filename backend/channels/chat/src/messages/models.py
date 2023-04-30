from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Message(BaseModel):
    """ Message model """
    id: Optional[ObjectId] = Field(alias="_id")
    sender_id: ObjectId = Field(...)
    room_id: ObjectId = Field(...)
    message_text: str = Field(...)
    created_at: datetime = Field(default=datetime.utcnow())

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "sender_id": "6148ed23aa02a1a38bde5e5d",
                "room_id": "6148ed23aa02a1a38bde5e5c",
                "message_text": "Hello, world!",
                "created_at": "2023-04-22T12:00:00.000Z"
            }
        }
