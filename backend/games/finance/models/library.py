from django.db import models
from core.models import Product


class Library(models.Model):
    user = models.UUIDField('User', unique=True)
    games_count = models.PositiveBigIntegerField(type=int)
    dlc_count = models.PositiveBigIntegerField(type=int)
    total_product_count = models.PositiveBigIntegerField(type=int)
    products = models.ManyToManyField(Product, related_name='library', through='LibraryProduct')

    class Meta:
        db_table = "library"


class LibraryProduct(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
