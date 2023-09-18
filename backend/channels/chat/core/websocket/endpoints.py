from fastapi import Depends
from src.middlewares import get_token

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from core.websocket.handlers.connection import ConnectionContextManager
from core.websocket.handlers.producer import ProducerHandler


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