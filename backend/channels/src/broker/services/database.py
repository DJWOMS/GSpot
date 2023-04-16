from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    def __init__(self):
        self.url = 'mongodb://Channels:password@mongodb:27017/GSpot?authSource=admin'

    async def connect(self):
        self.client = AsyncIOMotorClient(self.url, maxPoolSize=10, minPoolSize=10)

    async def disconnect(self):
        self.client.close()


db = MongoManager()

