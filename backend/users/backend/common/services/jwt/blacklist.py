class TokenBlackList:
    def __init__(self, token: str):
        self.token = token

    def add(self):
        raise NotImplementedError
