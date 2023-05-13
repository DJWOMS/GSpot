from common.services.jwt.token import Token


class TokenBlackList:
    def __init__(self, token: str):
        self.token = token

    def add(self):
        Token().check_token(self.token)
        pass
