from django.db import models
from core.models import Product


class Library(models.Model):
    user = models.UUIDField('User', unique=True)
    games_count = models.PositiveBigIntegerField('Games counter', default=0)
    dlc_count = models.PositiveBigIntegerField('DLC counter', default=0)
    total_product_count = models.PositiveBigIntegerField('Total product counter', default=0)
    products = models.ManyToManyField(Product, related_name='library', through='LibraryProduct')

    class Meta:
        db_table = "library"


class LibraryProduct(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
