from fastapi.websockets import WebSocketDisconnect
import redis

from config.redis import radis_config


class RedisSettings:
    def __init__(self):
        self.redis_cli = redis.Redis(host=radis_config.host, port=radis_config.port)
        self.pubsub = self.redis_cli.pubsub()

    async def consumer_handler(self, message: str, token: str):
        try:
            self.redis_cli.publish(token, message)
        except WebSocketDisconnect as exc:
            print(exc)

    async def producer_handler(self, token: str):
        self.pubsub.subscribe(token)
        try:
            message = self.pubsub.get_message()
            while message and message['type'] != 'message':
                message = self.pubsub.get_message()
                return message.get('data')
        except Exception as exc:
            print(exc)

    async def unsubscribe(self):
        self.pubsub.unsubscribe("chat:c")


redis_conn = RedisSettings()
