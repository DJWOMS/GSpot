from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from utils.models import PydanticObjectId


class Message(BaseModel):
    """ Message model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    sender_id: PydanticObjectId
    room_id: PydanticObjectId
    message_text: str
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
