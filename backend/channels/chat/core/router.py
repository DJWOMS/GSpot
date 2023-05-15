from fastapi import APIRouter
from core.websocket.router.route import ws


router = APIRouter()
router.include_router(ws, tags=('websocket',))
