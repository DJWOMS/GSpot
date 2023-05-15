from fastapi import FastAPI
from core.websocket.router.router import core_wsrouter, ws
from core.database import db
from core.websocket.router.routing import WebSocketRouter


app = FastAPI()

app.include_router(ws)

chat = WebSocketRouter()
chat.include_router(core_wsrouter)


@app.on_event('startup')
async def init_db():
    db.session = await db.client.start_session()
