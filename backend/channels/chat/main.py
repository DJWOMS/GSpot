from fastapi import FastAPI
from gspot_fastapi_auth.providers import RedisSingleton
from contextlib import asynccontextmanager

from core.router import ws_router, router
from core.database import db
from core.websocket.router.routing import WebSocketRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    RedisSingleton()
    yield
    await RedisSingleton().close()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

chat = WebSocketRouter()

chat.include_router(ws_router)


@app.on_event('startup')
async def init_services():
    db.session = await db.client.start_session()


