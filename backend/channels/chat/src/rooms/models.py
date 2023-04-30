from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Room(BaseModel):
    """ Room model """
    id: Optional[ObjectId] = Field(alias="_id")
    room_name: str = Field(...)
    created_at: datetime = Field(default=datetime.utcnow())

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "room_name": "Test Room",
                "created_at": "2023-04-22T12:00:00.000Z"
            }
        }
