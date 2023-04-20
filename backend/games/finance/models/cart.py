
from django.db import models
from finance.models.offer import Offer


class Cart(models.Model):
    created_by = models.UUIDField(unique=True)
    is_gift = models.BooleanField(default=False)

    class Meta:
        db_table = 'cart'


class CartOffer(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_offers')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='cart_offers')

    class Meta:
        db_table = 'cart_offer'
