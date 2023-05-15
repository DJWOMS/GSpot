import typing


class Router:
    def __init__(self, endpoint: typing.Callable, name: str):
        pass


class WebsocketRouter:
    def __init__(self, routes: typing.Optional[typing.Sequence[Router]] = None):
        self.router = []
