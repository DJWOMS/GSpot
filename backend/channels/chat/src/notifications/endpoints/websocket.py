from core.websocket.router.routing import WebSocketRouter

from ..repository import NotificationRepo

notifications = WebSocketRouter()


@notifications.add_endpoint('notifications')
async def test_notifications(request):
    pass
    # await websocket.send_text('функция notifications отработала')


@notifications.add_endpoint('update_status')
async def update_status_notification(request):
    await NotificationRepo.update_status_notification(
        _id=request.body.get('id'),
        status=request.body.get('status'),
    )
