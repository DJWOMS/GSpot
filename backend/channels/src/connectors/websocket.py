import asyncio

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
                await pubsub.psubscribe('channel:*')

                async def wait_websocket():
                    while True:
                        message = await websocket.receive_text()
                        await pubsub.publish('channel:*', message)
                        await websocket.send_text(f"Message text was: {message}")

                async def wait_pubsub():
                    while True:
                        message = await pubsub.get_message(ignore_subscribe_messages=True)
                        if message:
                            channel = message['channel'].decode()
                            data = message['data'].decode()
                            await websocket.send_text(f'Channel: {channel}, Message: {data}')

                # Когда мы передаем управлению потоку, то соединение сразу же обрывается, при этом нужно держать сразу 2 бесконечных await

                await asyncio.wait([
                    wait_pubsub(),
                    wait_websocket()
                ])

        except WebSocketDisconnect:
            print('client disconnected')

    async def send_personal_message(self, message: str, uuid: str):
        await self.connection.publish(uuid, message)

    async def broadcast(self, message: str):
        await self.connection.publish('broadcast', message)


websocket_manager = ConnectionManager()
