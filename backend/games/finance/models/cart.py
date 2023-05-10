from django.db import models
from finance.models.offer import Offer


class Cart(models.Model):
    created_by = models.UUIDField(unique=True)
    gift_recipient = models.UUIDField(blank=True, null=True)
    frozen = models.BooleanField(default=False)
    offers = models.ManyToManyField(Offer, related_name='cart', through='CartOffer')

    class Meta:
        db_table = 'cart'


class CartOffer(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_offers')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='cart_offers')

    class Meta:
        db_table = 'cart_offer'
