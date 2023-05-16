import typing


class BaseRoute:
    endpoint: typing.Callable
    path: str

    def __init__(self, path: str, endpoint: typing.Callable[..., typing.Any]):
        self.path = path
        self.endpoint = endpoint


class WebSocketRouter:

    def __init__(self, routes: typing.Optional[typing.Sequence[BaseRoute]] = None,):
        self.routes = []

    def add_endpoint(self, path: str):
        def decorator(endpoint: typing.Callable[..., typing.Any]):
            self.add_route(path, endpoint)
            return endpoint
        return decorator

    def include_router(self, router: "WebSocketRouter"):
        for route in router.routes:
            self.routes.append(route)

    def add_route(self, path: str, func: typing.Callable):
        self.routes.append(BaseRoute(path, func))

    async def handle(self, request):
        for route in self.routes:
            if route.path == request.path:
                await route.endpoint(request)
            # else:
            #     await websocket.send_text('no such router')