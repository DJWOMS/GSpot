from fastapi import APIRouter
from core.websocket.endpoints import ws
from core.websocket.router.routing import WebSocketRouter
from src.messages.endpoints.websocket import messages


ws_router = WebSocketRouter()
ws_router.include_router(messages)

router = APIRouter()
router.include_router(ws, tags=('websocket',))
