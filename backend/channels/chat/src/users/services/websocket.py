from fastapi import WebSocket

from src.users.services.redis_pubsub import redis_conn


class ConnectionManager:

    @staticmethod
    async def consume(websocket: WebSocket, token: str):
        message = await websocket.receive_text()
        if message:
            await redis_conn.consumer_handler(message=message, token=token)

    @staticmethod
    async def produce(websocket: WebSocket, token: str):
        message = await redis_conn.producer_handler(token=token)
        await websocket.send_text(f"Client #{token} says: {message}")

    @staticmethod
    async def unsubscribe():
        await redis_conn.unsubscribe()


manager = ConnectionManager()
