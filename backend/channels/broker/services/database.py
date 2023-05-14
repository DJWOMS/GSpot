from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:



    async def ping_server(self, client):
        try:
            client.GSpot.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


db = MongoManager()