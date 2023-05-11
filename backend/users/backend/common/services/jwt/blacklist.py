class TokenBlackList:
    def __init__(self, token: str):
        self.token = token

    def add(self, refresh_token: str):
        raise NotImplementedError
