from django.db import models


class BaseTextChoices(models.TextChoices):
    @classmethod
    def max_length(cls):
        return max([len(v) for v in cls.values])


class CurrencyChoices(BaseTextChoices):
    RUB = "RUB", "Rub"
    USD = "USD", "Usd"
    KZT = "KZT", "Kzt"
    EUR = "EUR", "Eur"


class GradeChoices(BaseTextChoices):
    LIKE = 'LIKE', 'Like'
    DISLIKE = 'DISLIKE', 'Dislike'


class TypeProductChoices(BaseTextChoices):
    GAMES = 'GAMES', 'Games'
    DLC = 'DLC', 'Additions'
