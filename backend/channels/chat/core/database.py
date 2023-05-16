from config.database import db_config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = AsyncIOMotorClient(db_config.url, maxPoolSize=10, minPoolSize=10)
    session: AsyncIOMotorDatabase

    async def ping_server(self):
        try:
            self.client.GSpot.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


db = MongoManager()
