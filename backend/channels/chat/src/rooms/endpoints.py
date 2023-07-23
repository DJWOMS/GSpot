from fastapi import APIRouter, Depends

from ..middlewares import get_user_or_403
from .services import get_room_messages

room = APIRouter(prefix='/room', tags=['Room'])


@room.get('/{room_id}/{token}', dependencies=[Depends(get_user_or_403)])
async def chat_room(room_id: str):
    """All room message history"""
    messages = await get_room_messages(room_id)
    return messages
