from pydantic import BaseSettings


class GamesService(BaseSettings):
    GAMES_DOMAIN: str
    GAMES_REFUND: str

    @property
    def get_refund_url(self):
        return f'{self.GAMES_DOMAIN}{self.GAMES_REFUND}'


GAMES_SERVICE = GamesService()
