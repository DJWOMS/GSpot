from django.db import models
from core.models import Product
from finance.models import Offer


class Library(models.Model):
    user = models.UUIDField('User', unique=True)
    games_count = models.PositiveIntegerField('Games counter', default=0)
    dlc_count = models.PositiveIntegerField('DLC counter', default=0)
    total_product_count = models.PositiveIntegerField('Total product counter', default=0)
    products = models.ManyToManyField(Product, related_name='library', through='LibraryProduct')

    class Meta:
        db_table = "library"


class LibraryProduct(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    can_return = models.BooleanField(default=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'library_product'
