"""User, RoomParticipant"""

from datetime import datetime
from typing import Optional

from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field


class ChatStatus(str, Enum):
    """Возможные варианты статуса пользователя в чате.
    При попытке установить значение, которого нет в этом списке,
    будет возбуждено исключение ValueError."""

    ONLINE = "В сети"
    OFFLINE = "Не в сети"
    AWAY = "Отошёл"
    INVISIBLE = "Инкогнито"


class User(BaseModel):
    """Модель пользователя."""
    id: Optional[ObjectId] = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    avatar: Optional[str] = Field(default=None)
    last_seen: Optional[datetime] = Field(default=datetime.utcnow())
    chat_status: str = Field(default=ChatStatus.OFFLINE)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "email": "johndoe@example.com",
                "password": "secretpassword",
                "avatar": "https://example.com/avatar.png",
                "last_seen": "2023-04-22T12:00:00.000Z",
                "chat_status": "В сети",
            }
        }


class RoomParticipant(BaseModel):
    """Модель участника комнаты."""
    id: Optional[ObjectId] = Field(alias="_id")
    user_id: ObjectId = Field(...)
    room_id: ObjectId = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "user_id": "6148ed23aa02a1a38bde5e5d",
                "room_id": "6148ed23aa02a1a38bde5e5c",
            }
        }
