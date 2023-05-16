from core.websocket.router.routing import WebSocketRouter


messages = WebSocketRouter()


@messages.add_endpoint('test')
async def test_message(request, websocket):
    print(request)
    await websocket.send_text('функция тест отработала и вернула результат')



