import asyncio
from fastapi import (
    APIRouter,
    WebSocket,
    Depends,
    WebSocketDisconnect,
)

from src.users.services import manager
from middlewares import get_token


ws_router = APIRouter()


@ws_router.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        token: str = Depends(get_token),
):
    await websocket.accept()
    try:
        while True:
            await manager.consume(websocket=websocket, token=token)
            await manager.produce(websocket=websocket, token=token)
    except WebSocketDisconnect:
        await manager.unsubscribe()
