from common.services.jwt.token import Token


class TokenBlackList:
    def __init__(self, token: str):
        self.token = token

    def add(self):
        token = Token()
        token.check_token(self.token)
        ttl = token.check_exp_left(self.token)
        ttl
