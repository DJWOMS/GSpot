from pydantic import BaseSettings


class GamesService(BaseSettings):
    GAMES_DOMAIN: str
    GAMES_REFUND: str
    CANCEL_GIFT: str

    @property
    def refund_url(self) -> str:
        return f'{self.GAMES_DOMAIN}{self.GAMES_REFUND}'

    @property
    def cancel_gift_url(self) -> str:
        return f'{self.GAMES_DOMAIN}{self.CANCEL_GIFT}'


GAMES_SERVICE = GamesService()
