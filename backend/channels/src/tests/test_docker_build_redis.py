import pytest
from redis_consumer import Redis
from redis_consumer.asyncio import Redis as RedisAsyncio


@pytest.mark.usefixtures("redis_test_client")
def test_redis_database_connection(redis_test_client: Redis):
    record_name, record_value = "Message", "Redis message"

    redis_test_client.set(name=record_name, value=record_value)
    message = redis_test_client.get(name=record_name)
    redis_test_client.flushdb()

    assert message.decode() == record_value


@pytest.mark.usefixtures("redis_test_asyncio_client")
async def test_redis_asyncio_database_connection(redis_test_asyncio_client: RedisAsyncio):
    record_name, record_value = "Message", "Redis message"

    async with redis_test_asyncio_client.pipeline(transaction=True) as pipe:
        await pipe.set(name=record_name, value=record_value).execute()
        messages = await pipe.get(name=record_name).execute()
        await pipe.flushdb().execute()

    assert messages[0].decode() == record_value
