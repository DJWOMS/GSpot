from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
from utils.models import PydanticObjectId


class Message(BaseModel):
    """ Message model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    sender_id: PydanticObjectId
    room_id: PydanticObjectId
    message_text: str
    created_at: datetime = Field(default=datetime.utcnow())

    @validator('message_text')
    def validate_message_text(cls, v):
        if not v.strip():
            raise ValueError("Message mustn't be empty.")
        return v

    @validator('created_at')
    def validate_created_at(cls, v):
        try:
            datetime.strptime(str(v), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError as e:
            raise ValueError("Invalid created_at format. Expected format: YYYY-MM-DDTHH:MM:SS.sssZ") from e

        if v > datetime.utcnow():
            raise ValueError("created_at can't be in the future.")
        return v

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
