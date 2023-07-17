from django.db import models
from django.db.models import ProtectedError

from simple_history.models import HistoricalRecords

from core.models import Product


class Genre(models.Model):
    name = models.CharField('Genre', max_length=50, unique=True, db_index=True)
    products = models.ManyToManyField(Product, related_name='genres', through='GenreProduct')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.products.exists():
            raise ProtectedError("Cannot delete Genre. It has associated products.", self)
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'genre'


class SubGenre(models.Model):
    name = models.CharField('Subgenre', max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='subgenres')
    products = models.ManyToManyField(Product, related_name='subgenres', through='SubgenreProduct')
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        if self.products.exists():
            raise ProtectedError("Cannot delete SubGenre. It has associated products.", self)
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'subgenre'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'genre'],
                name='unique_genre_subgenre'
            )
        ]


class SubgenreProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subgenre_product'
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'subgenre'],
                name='unique_subgenre_product'
            )
        ]


class GenreProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'genre_product'
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'genre'],
                name='unique_genre_product'
            )
        ]
