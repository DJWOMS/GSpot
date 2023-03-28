from typing import Mapping, Any
import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient
from pymongo.database import Database
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import redis
import redis.asyncio as redis_asyncio
import pika
import aio_pika
from main import app
from config.settings import settings
from src.utils.test_connection import ping, websocket_ping


pytest_plugins = ("celery.contrib.pytest",)


client = TestClient(app)


@pytest.fixture
async def add_api_test_connection():
    """
    Fixture to create temprorary api ping router.
    """
    app.add_api_route("/ping", ping)
    yield
    app.router.routes.pop()


@pytest.fixture
async def add_websocket_test_connection():
    """
    Fixture to create temprorary websocket ping router.
    """
    app.add_websocket_route("/ws/ping", websocket_ping)
    yield
    app.router.routes.pop()


@pytest.fixture
def pymongo_test_database() -> Database:
    """
    Fixture to create test database with pymongo.
    """
    with MongoClient(settings.MONGODB_URL) as mongo_client:
        mongo_db = mongo_client[settings.MONGODB_TEST_DATABASE]
        yield mongo_db
        mongo_client.drop_database(settings.MONGODB_TEST_DATABASE)


@pytest.fixture
async def motor_test_database() -> AsyncIOMotorDatabase:
    """
    Fixture to create test database with motor.
    """
    mongo_client = AsyncIOMotorClient(settings.MONGODB_URL)
    mongo_db = mongo_client[settings.MONGODB_TEST_DATABASE]
    yield mongo_db
    mongo_client.drop_database(settings.MONGODB_TEST_DATABASE)
    mongo_client.close()


@pytest.fixture
def redis_test_client():
    """
    Fixture to create test redis client connection.
    """
    with redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                     db=settings.REDIS_TEST_DATABASE_INDEX) as redis_client:
        yield redis_client
        redis_client.flushdb()


@pytest.fixture
async def redis_test_asyncio_client():
    """
    Fixture to create test redis asyncio client connection.
    https://redis-py.readthedocs.io/en/stable/examples/asyncio_examples.html
    """
    connection = redis_asyncio.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                                     db=settings.REDIS_TEST_DATABASE_INDEX)
    yield connection
    await connection.close()


@pytest.fixture
def pika_test_connection():
    """
    Fixture to create test pika connection.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_LOCAL_HOST_NAME,
            port=settings.RABBITMQ_LOCAL_PORT,
            credentials=pika.PlainCredentials(
                username=settings.RABBITMQ_DEFAULT_USER,
                password=settings.RABBITMQ_DEFAULT_PASS
            )
        )
    )
    yield connection
    connection.close()


@pytest.fixture
async def aio_pika_test_connection():
    """
    Fixture to create test aio_pika connection.
    """
    connection = await aio_pika.connect_robust(
        host=settings.RABBITMQ_LOCAL_HOST_NAME,
        port=settings.RABBITMQ_LOCAL_PORT,
        login=settings.RABBITMQ_DEFAULT_USER,
        password=settings.RABBITMQ_DEFAULT_PASS
    )
    yield connection
    await connection.close()


@pytest.fixture(scope='session')
def celery_config():
    """
    Celery test app configuration fixture.
    """
    return {
        'broker_url': 'redis://redis:6379',
        'result_backend': 'redis://redis:6379'
    }


@pytest.fixture
def celery_worker_parameters():
    # type: () -> Mapping[str, Any]
    """Redefine this fixture to change the init parameters of Celery workers.

    This can be used e.g. to define queues the worker will consume tasks from.

    The dict returned by your fixture will then be used
    as parameters when instantiating :class:`~celery.worker.WorkController`.
    """
    return {
        # For some reason this `celery.ping` is not registed IF our own worker is still
        # running. To avoid failing tests in that case, we disable the ping check.
        # see: https://github.com/celery/celery/issues/3642#issuecomment-369057682
        # here is the ping task: `from celery.contrib.testing.tasks import ping`
        'perform_ping_check': False,
    }
