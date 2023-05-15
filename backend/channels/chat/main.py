from fastapi import FastAPI
from core.database import db
from core.router import core_wsrouter, router
from core.websocket.router.routing import WebSocketRouter


app = FastAPI()

app.include_router(router)

chat = WebSocketRouter()
chat.include_router(core_wsrouter)


@app.on_event('startup')
async def init_db():
    db.session = await db.client.start_session()
