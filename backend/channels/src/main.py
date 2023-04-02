from config import RABBIT_URL
from fastapi import FastAPI
from aio_pika import connect_robust
from pika import schemas as pika_schemas
from utils.send_message import send_messages


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.connection = await connect_robust(RABBIT_URL)
    app.state.channel = await app.state.connection.channel(publisher_confirms=False)


@app.on_event("shutdown")
async def shutdown():
    if not app.state.channel.is_closed:
        await app.state.channel.close()
    if not app.state.connection.is_closed:
        await app.state.connection.close()


@app.post('/test')
async def process():
    message = pika_schemas.AioMessage(type='test')
    await send_messages(app.state.channel, message.dict())

    return {'result': 'Success'}
