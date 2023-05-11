import functools
import json
import logging
from fastapi import WebSocket
import redis.asyncio as redis
from redis.asyncio.client import PubSub, Redis

from config.redis import redis_config


def ps_wrap(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        async with args[0].pubsub as pubsub:
            await func(args[0], pubsub, **kwargs)

    return wrapper


class ConnectionContextManager:
    websocket: WebSocket
    user_id: str
    redis: Redis = redis.from_url(
        redis_config.url,
        encoding='utf-8',
        decode_responses=True
    )
    pubsub: PubSub

    def __init__(self, websocket: WebSocket, user_id: str):
        self.user_id = user_id
        self.websocket = websocket
        self.pubsub = self.redis.pubsub()

    async def _connect(self):
        await self.websocket.accept()
        await self.redis.set(f'status:{self.user_id}', '1')
        await self.pubsub.subscribe(f'channel:{self.user_id}')

    async def _disconnect(self):
        await self.redis.delete(f'status:{self.user_id}')
        await self.pubsub.unsubscribe(f'channel:{self.user_id}')
        await self.websocket.close()
        await self.pubsub.close()

    async def send_message(self, *, content: str):
        try:
            payload = json.loads(content)
            await self.websocket.send_json(payload)
        except json.JSONDecodeError:
            raise Exception('Failed to parse websocket payload')

    async def __aenter__(self):
        logging.debug('Context manager enter')
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._disconnect()
        logging.debug('Context manager exit')
