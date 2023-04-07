from fastapi import WebSocket, WebSocketDisconnect
import redis.asyncio as redis

from config import settings


class ConnectionManager:
    def __init__(self):
        self.connection = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DATABASE,
            decode_responses=True
        )

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        await self.subscribe(websocket)

    async def subscribe(self, websocket: WebSocket):
        try:
            async with self.connection.pubsub() as pubsub:
                while True:
                    await pubsub.psubscribe('channel:*')
                    while True:
                        message = await websocket.receive_text()
                        await websocket.send_text(f"Message text was: {message}")
                        message = await pubsub.get_message(ignore_subscribe_messages=True)
                        if message:
                            channel = message['channel'].decode()
                            data = message['data'].decode()
                            await websocket.send_text(f'Channel: {channel}, Message: {data}')

        except WebSocketDisconnect:
            print('client disconnected')

    async def send_personal_message(self, message: str, uuid: str):
        await self.connection.publish(uuid, message)

    async def broadcast(self, message: str):
        await self.connection.publish('broadcast', message)


websocket_manager = ConnectionManager()
