import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from core.websocket.handlers.connection import ConnectionContextManager
from core.websocket.handlers.producer import ProducerHandler
from src.middlewares import get_token

ws = APIRouter()


@ws.websocket('/ws/{token}/')
async def websocket_handler(websocket: WebSocket, token: str = Depends(get_token)):
    async with ConnectionContextManager(user_id=token, websocket=websocket) as service:
        user_id = token
        producer = ProducerHandler()
        while True:
            try:
                message = await service.pubsub.get_message()
                if message is not None:
                    if type(message['data']) is not int:
                        await websocket.send_text(message['data'])
                data = await websocket.receive_json()
                data['user_id'] = user_id
                await producer.handle_event(data)
            except RuntimeError:
                break
            except WebSocketDisconnect:
                break