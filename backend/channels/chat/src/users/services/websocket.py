from fastapi import WebSocket

from config.settings import redis_conn


class ConnectionManager:

    @staticmethod
    async def consume(websocket: WebSocket, token: str):
        await redis_conn.consumer_handler(ws=websocket, token=token)

    @staticmethod
    async def produce(websocket: WebSocket, token: str):
        await redis_conn.producer_handler(ws=websocket, token=token)

    @staticmethod
    async def unsubscribe():
        await redis_conn.unsubscribe()


manager = ConnectionManager()
