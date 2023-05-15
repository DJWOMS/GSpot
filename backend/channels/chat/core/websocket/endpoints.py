from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from core.websocket.connect_user import ConnectionContextManager
from core.websocket.handlers.producer import ProducerHandler

ws = APIRouter()


@ws.websocket('/ws')
async def websocket_handler(websocket: WebSocket):
    async with ConnectionContextManager(user_id='token[:10]', websocket=websocket) as service:
        producer = ProducerHandler(websocket)
        while True:
            try:
                data = await websocket.receive_json()
                await producer.handle_event(data)
            except WebSocketDisconnect:
                break
            except RuntimeError:
                break


