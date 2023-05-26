from fastapi import (
    Query,
    WebSocketException,
    status,
)
import aiohttp


async def get_token(token):
    print(token)
    return token


# async def get_token(
#     token: str | None = Query(default=None),
# ):
#     print(token)
#     return True
    # async with aiohttp.ClientSession() as session:
    #     async with session.post('http://users/token', json={'token': token}) as resp:
    #         if resp.status != 201:
    #             raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    # return token
