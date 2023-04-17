
from django.db import models
from finance.models.offer import Offer


class Cart(models.Model):
    CHOICES = (
        ("True", True),
        ("False", False),
    )

    created_by = models.UUIDField('UUID creator', unique=True)
    is_gift = models.CharField(choices=CHOICES, max_length=10)

    class Meta:
        db_table = 'cart'


class CartOffer(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_offer'
