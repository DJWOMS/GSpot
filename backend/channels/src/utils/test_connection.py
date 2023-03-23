from fastapi.websockets import WebSocket
from fastapi import APIRouter, status


test_connection_router = APIRouter(
    prefix="/test_connection",
    tags=["Test connection"]
)


@test_connection_router.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    """
    Api method to test the docker fastapi connection.
    test_connection_router is not present in fastapi app by default.
    The Api route of this function is only added to the fastapi application during testing.
    (See fixtures in the tests/conftest.py).
    """
    return {"message": "pong"}


@test_connection_router.websocket("/ws/ping")
async def websocket_ping(websocket: WebSocket):
    """
    Api method to test the docker fastapi connection.
    test_connection_router is not present in fastapi app by default.
    The Websocket route of this function is only added to the fastapi application during testing.
    (See fixtures in the tests/conftest.py).
    """
    await websocket.accept()
    await websocket.send_json({"message": "pong"})
    await websocket.close()
