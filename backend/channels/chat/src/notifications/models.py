from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
from utils.models import PydanticObjectId


class Notification(BaseModel):
    """ Notification model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    user_id: PydanticObjectId
    text: str
    status: str = Field(default="unread")
    timestamp: datetime = Field(default=datetime.utcnow())
    timestamp_2: datetime = Field(default=datetime.utcnow())

    @validator('text')
    def validate_text(cls, v):
        if not v.strip():
            raise ValueError("Message mustn't be empty.")
        return v

    @validator('status')
    def validate_status(cls, v):
        if v not in ['unread', 'read']:
            raise ValueError('Invalid status. Status must be one of "["unread", "read"]".')
        return v

    @validator('timestamp', 'timestamp_2')
    def validate_timestamp(cls, values):
        timestamp = values.get('timestamp')
        timestamp_2 = values.get('timestamp_2')

        try:
            datetime.strptime(str(timestamp), '%Y-%m-%dT%H:%M:%S.%fZ')
            datetime.strptime(str(timestamp_2), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError as e:
            raise ValueError("Invalid timestamp format. Expected format: YYYY-MM-DDTHH:MM:SS.sssZ") from e

        if timestamp > datetime.utcnow() or timestamp_2 > datetime.utcnow():
            raise ValueError("Timestamps can't be in the future.")

        return values

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
