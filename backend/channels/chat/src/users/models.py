from datetime import datetime
from typing import Optional

from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field


class ChatStatus(str, Enum):
    """ Chat status enum """

    ONLINE = "online"
    OFFLINE = "offline"
    AWAY = "away"
    INVISIBLE = "invisible"


class User(BaseModel):
    """ User model """

    id: ObjectId = Field(alias="_id")
    username: str
    avatar: Optional[str] = Field(default=None)
    last_seen: Optional[datetime] = Field(default=datetime.utcnow())
    chat_status: str = Field(default=ChatStatus.OFFLINE)

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
    id: Optional[ObjectId] = Field(alias="_id")
    user_id: ObjectId
    room_id: ObjectId

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "user_id": "6148ed23aa02a1a38bde5e5d",
                "room_id": "6148ed23aa02a1a38bde5e5c",
            }
        }
