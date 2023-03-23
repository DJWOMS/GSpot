import pytest
from pymongo.database import Database
from motor.motor_asyncio import AsyncIOMotorClient


@pytest.mark.usefixtures("pymongo_test_database")
def test_mongodb_pymongo(pymongo_test_database: Database):
    message_key, message_value = "Message", "Pymongo message"

    ins = pymongo_test_database.messages.insert_one({message_key: message_value})
    cursor = pymongo_test_database.messages.find_one(ins.inserted_id)
    pymongo_test_database.messages.delete_one(cursor)

    assert cursor[message_key] == message_value


@pytest.mark.usefixtures("motor_test_database")
async def test_mongodb_motor(motor_test_database: AsyncIOMotorClient):
    message_key, message_value = "Message", "Motor message"

    ins = await motor_test_database.messages.insert_one({message_key: message_value})
    cursor = await motor_test_database.messages.find_one(ins.inserted_id)
    await motor_test_database.messages.delete_one(cursor)

    assert cursor[message_key] == message_value
