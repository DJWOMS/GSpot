from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from connectors import rabbit_connection, websocket_manager
from schemas import pika as pika_schemas


@asynccontextmanager
async def lifespan(_: FastAPI):
    await rabbit_connection.connect()
    yield
    await rabbit_connection.disconnect()


app = FastAPI(lifespan=lifespan)


@app.post('/test')
async def process():
    message = pika_schemas.AioMessage(type='test')
    await rabbit_connection.send_messages(message.dict())

    return {'result': 'Success'}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket_manager.broadcast(f"Client {websocket.client.host} says: {data}")
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
        await websocket_manager.broadcast(f"Client {websocket.client.host} left the chat")
