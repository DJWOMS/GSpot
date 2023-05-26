from config.redis import redis_config
from redis.asyncio.client import PubSub, Redis
import redis.asyncio as rd


class RedisManager:
    redis: Redis = rd.from_url(
        redis_config.url,
        encoding='utf-8',
        decode_responses=True
    )
    pubsub: PubSub


redis_manager = RedisManager()
