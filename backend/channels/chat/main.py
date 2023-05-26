from fastapi import FastAPI
from core.database import db
from core.router import ws_router, router
from core.database import db
from core.websocket.router.routing import WebSocketRouter


app = FastAPI()

app.include_router(router)

chat = WebSocketRouter()

chat.include_router(ws_router)


@app.on_event('startup')
async def init_services():
    db.session = await db.client.start_session()

