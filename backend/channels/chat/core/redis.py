import json
from typing import Dict

import redis.asyncio as rd
from config.redis import redis_config
from redis.asyncio.client import PubSub, Redis


class RedisManager:
    redis: Redis = rd.from_url(
        redis_config.url,
        encoding='utf-8',
        decode_responses=True
    )
    pubsub: PubSub

    async def get(self, key: str, is_json: bool) -> Dict | str:
        if value := await self.redis.get(key):
            return json.loads(value) if is_json else value


redis_manager = RedisManager()
