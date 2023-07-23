import aiohttp
from core.redis import redis_manager
from fastapi import HTTPException
from src.rooms.services import get_room_participant
from starlette.status import HTTP_403_FORBIDDEN


async def get_token():
    pass


async def get_user_or_403(token: str) -> None | HTTPException:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'http://users.alpha.g-spot.website/api/v1/customer/customer/me',
            headers={'Authorization': token}
        ) as resp:
            if resp.status != 200:
                raise HTTPException(HTTP_403_FORBIDDEN)
    return


async def user_is_participant(room_id: str, token: str) -> None | HTTPException:
    """'get_room_participant` return `RoomParticipant` object or None"""
    if redis_payload := await redis_manager.get(f'basic:{token}', True):
        if await get_room_participant(room_id, redis_payload['user_id']):
            return
    raise HTTPException(HTTP_403_FORBIDDEN)
