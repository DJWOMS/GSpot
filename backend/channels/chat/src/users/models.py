from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, validator
from utils.models import PydanticObjectId


class ChatStatus(str, Enum):
    """ Chat status enum """

    ONLINE = "online"
    OFFLINE = "offline"
    AWAY = "away"
    INVISIBLE = "invisible"


class User(BaseModel):
    """ User model """

    id: PydanticObjectId = Field(alias="_id")
    username: str
    avatar: Optional[str] = Field(default=None)
    last_seen: Optional[datetime] = Field(default=datetime.utcnow())
    chat_status: str = Field(default=ChatStatus.OFFLINE)

    @validator('username')
    def validate_username(cls, v):
        if not v.split():
            raise ValueError("username musn't be empty.")
        return v

    @validator('last_seen')
    def validate_last_seen(cls, v):
        if v is not None:
            try:
                datetime.strptime(str(v), '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError as e:
                raise ValueError("Invalid last_seen format. Expected format: YYYY-MM-DDTHH:MM:SS.sssZ") from e
        if v > datetime.utcnow():
            raise ValueError("last_seen can't be in the future.")
        return v

    @validator('chat_status')
    def validate_chat_status(cls, v):
        if v not in ChatStatus._value2member_map_:
            raise ValueError(f'Invalid chat_status. chat_status must be one of "{list(ChatStatus._value2member_map_.keys())}".')
        return v

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "avatar": "https://example.com/avatar.png",
                "last_seen": "2023-04-22T12:00:00.000Z",
                "chat_status": "В сети",
            }
        }


class RoomParticipant(BaseModel):
    """ Room participant model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    user_id: PydanticObjectId
    room_id: PydanticObjectId

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "user_id": "6148ed23aa02a1a38bde5e5d",
                "room_id": "6148ed23aa02a1a38bde5e5c",
            }
        }
