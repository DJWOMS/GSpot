import aiohttp
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN


async def get_token():
    pass


async def get_user_or_403(token: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'http://users.alpha.g-spot.website/api/v1/customer/customer/me',
            headers={'Authorization': token}
        ) as resp:
            if resp.status != 200:
                raise HTTPException(HTTP_403_FORBIDDEN)
    return
