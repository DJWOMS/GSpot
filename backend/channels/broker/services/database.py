from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url):
        self.client = AsyncIOMotorClient(url, maxPoolSize=10, minPoolSize=10)

    async def disconnect(self):
        self.client.close()


db = MongoManager()

