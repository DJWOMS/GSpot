from django.db import models
from core.models import Product
from simple_history.models import HistoricalRecords


class Genre(models.Model):
    name = models.CharField('Genre', max_length=50, unique=True, db_index=True)
    products = models.ManyToManyField(Product, related_name='genres', through='GenreProduct')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'


class SubGenre(models.Model):
    name = models.CharField('Subgenre', max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='subgenres')
    products = models.ManyToManyField(Product, related_name='subgenres', through='SubgenreProduct')
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.name

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


class GenreProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
