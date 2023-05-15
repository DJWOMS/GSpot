import logging
from fastapi import WebSocket
from core.redis import redis
from redis.asyncio.client import PubSub, Redis


class ConnectionContextManager:
    websocket: WebSocket
    user_id: str
    redis_manager: Redis = redis
    pubsub: PubSub

    def __init__(self, websocket: WebSocket, user_id: str):
        self.user_id = user_id
        self.websocket = websocket
        self.redis_manager.pubsub = self.redis_manager.redis.pubsub()

    async def _connect(self):
        await self.websocket.accept()
        await self.redis_manager.redis.set(f'status:{self.user_id}', '1')
        await self.redis_manager.pubsub.subscribe(f'channel:{self.user_id}')

    async def _disconnect(self):
        await self.redis_manager.redis.delete(f'status:{self.user_id}')
        await self.redis_manager.pubsub.unsubscribe(f'channel:{self.user_id}')
        await self.websocket.close()
        await self.redis_manager.pubsub.close()

    async def __aenter__(self):
        logging.debug('Context manager enter')
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._disconnect()
        logging.debug('Context manager exit')