from fastapi import APIRouter, Depends

from ..middlewares import get_user_or_403, user_is_participant
from .services import get_room_messages

room = APIRouter(prefix='/room', tags=['Room'])


@room.get('/{room_id}/{token}/{user_id}', dependencies=[
    Depends(get_user_or_403), Depends(user_is_participant)
])
async def chat_room(room_id: str):
    """All room message history"""
    messages = await get_room_messages(room_id)
    return messages
