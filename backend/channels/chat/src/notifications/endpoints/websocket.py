from core.websocket.router.routing import WebSocketRouter


notifications = WebSocketRouter()


@notifications.add_endpoint('notifications')
async def test_notifications(request, websocket):
    await websocket.send_text('функция notifications отработала')