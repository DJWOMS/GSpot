from pydantic import BaseSettings

from .base import BASE_DIR, DEBUG


class RollbarAccessToken(BaseSettings):
    ROLLBAR_ACCESS_TOKEN: str

    @property
    def r_token(self):
        return self.ROLLBAR_ACCESS_TOKEN


rollbar_token = RollbarAccessToken()


ROLLBAR = {
    'access_token': rollbar_token.r_token,
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
