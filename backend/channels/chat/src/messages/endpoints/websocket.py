from core.websocket.router.routing import WebSocketRouter
from core.redis import redis_manager


messages = WebSocketRouter()


@messages.add_endpoint('test')
async def send_message(request):
    text = request.body['message_text']
    await redis_manager.redis.publish(request.body['reciever'], text)
