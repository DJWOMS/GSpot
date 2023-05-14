from config.redis import redis_config
from redis.asyncio.client import PubSub, Redis
import redis.asyncio as redis


class RedisManager:
    redis: Redis = redis.from_url(
        redis_config.url,
        encoding='utf-8',
        decode_responses=True
    )
    pubsub: PubSub


redis = RedisManager()
