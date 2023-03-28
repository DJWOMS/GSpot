import asyncio
from config import settings, RABBIT_URL
from fastapi import FastAPI
from aio_pika import connect_robust, Message

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.connection = await connect_robust(
        RABBIT_URL, loop=asyncio.get_event_loop()
    )


@app.on_event("shutdown")
async def shutdown():
    if not app.state.channel.is_closed:
        await app.state.channel.close()
    if not app.state.connection.is_closed:
        await app.state.connection.close()


@app.post('/test')
async def process():
    async with app.state.connection:
        channel = await app.state.connection.channel()
        await channel.default_exchange.publish(
            Message(body=f"Hello {settings.RABBITMQ_TEST_QUEUE}".encode()),
            routing_key=settings.RABBITMQ_TEST_QUEUE,
        )
    return {'result': 'Success'}
