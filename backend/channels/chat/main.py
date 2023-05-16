from fastapi import FastAPI
<<<<<<< HEAD
from src.router import router
from services.database import db
=======
from core.database import db
from core.router import ws_router, router
from core.websocket.router.routing import WebSocketRouter
>>>>>>> channels


app = FastAPI()

app.include_router(router)

<<<<<<< HEAD
=======
chat = WebSocketRouter()
chat.include_router(ws_router)

>>>>>>> channels

@app.on_event('startup')
async def init_db():
    db.session = await db.client.start_session()
