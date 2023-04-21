from fastapi import (
    FastAPI,
    WebSocket,
    Depends,
    WebSocketDisconnect,
)

from src import manager, get_token


app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        token: str = Depends(get_token),
):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{token} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{token} left the chat")
