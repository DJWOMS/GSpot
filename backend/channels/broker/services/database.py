from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url):
        self.client = AsyncIOMotorClient(url, maxPoolSize=10, minPoolSize=10)

    async def disconnect(self):
        self.client.close()

    async def ping_server(self):
        # Replace the placeholder with your Atlas connection string
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


db = MongoManager()

