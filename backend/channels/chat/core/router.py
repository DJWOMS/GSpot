from fastapi import APIRouter
from core.websocket.endpoints import ws
from core.websocket.router.routing import WebSocketRouter
from src.messages.endpoints.websocket import messages
from src.notifications.endpoints.websocket import notifications as ws_notifications
from src.notifications.endpoints.http import notification as http_notifications


ws_router = WebSocketRouter()
ws_router.include_router(messages)
ws_router.include_router(ws_notifications)

router = APIRouter()
router.include_router(ws, tags=('websocket',))
router.include_router(http_notifications)
