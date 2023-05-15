from core.websocket.router.routing import WebSocketRouter


notifications = WebSocketRouter()


@notifications.add_endpoint('notification')
async def test_notifications(request, websocket):
    print('async notif func is working')