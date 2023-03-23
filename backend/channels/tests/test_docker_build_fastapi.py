import pytest
from httpx import AsyncClient
from main import app
from tests.conftest import client


@pytest.mark.usefixtures("add_api_test_connection")
def test_fast_api_ping_sync():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


@pytest.mark.usefixtures("add_api_test_connection")
async def test_fast_api_ping_async():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


@pytest.mark.usefixtures("add_websocket_test_connection")
def test_websocket():
    with client.websocket_connect("/ws/ping") as websocket:
        assert websocket.receive_json() == {"message": "pong"}
