import asyncio
import redis.asyncio as redis

from config import settings


async def reader():
    connection = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DATABASE,
        decode_responses=True
    )
    async with connection.pubsub() as pubsub:
        await pubsub.subscribe('channel:*')

        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True)
            if message:
                print(f"(Reader) Message Received: {message}")


if __name__ == '__main__':
    asyncio.run(reader())
