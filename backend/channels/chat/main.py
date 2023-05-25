from fastapi import FastAPI
from core.router import ws_router, router
from core.database import db
from core.websocket.router.routing import WebSocketRouter
from src.notifications.endpoints.http import notification

app = FastAPI()

app.include_router(router)
app.include_router(notification)

chat = WebSocketRouter()

chat.include_router(ws_router)


@app.on_event('startup')
async def init_services():
    db.session = await db.client.start_session()


