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


class OrderStatusChoices(BaseTextChoices):
    WAITING_PAYMENT = "WAITING_PAYMENT", "Waiting Payment"
    COMPLETED = "COMPLETED", "Completed"
    CANCELED = "CANCELED", "Canceled"
    REFUND_REQUESTED = "REFUND_REQUESTED", "Refund Requested"
    REFUNDED = "REFUNDED", "Refunded"
