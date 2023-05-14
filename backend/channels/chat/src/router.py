import asyncio

from fastapi import APIRouter, WebSocket, Query

from core.handlers import producer_handler, consumer_handler
from core.utils import ConnectionContextManager

router = APIRouter()


@router.get('/test')
async def test():
    return {"message": "ok"}


@router.websocket('/ws')
async def websocket_handler(websocket: WebSocket, token: str = Query(...)):
    # Todo: parse token from query and extract real user id
    
    async with ConnectionContextManager(user_id=token[:10], websocket=websocket) as service:
        producer_task = asyncio.ensure_future(producer_handler(service))
        consumer_task = asyncio.ensure_future(consumer_handler(service))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()
