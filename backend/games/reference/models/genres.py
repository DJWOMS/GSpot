from django.db import models
from core.models import Product


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    products = models.ManyToManyField(Product, related_name='genres', through='SubgenreProduct')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_genre'
            )
        ]


class SubGenre(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='subgenres')
    products = models.ManyToManyField(Product, related_name='subgenre', through='SubgenreProduct')

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'genre'],
                name='unique_genre_subgenre'
            )
        ]


class SubgenreProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    subgenre = models.ForeignKey(
        SubGenre,
        on_delete=models.CASCADE,
        related_name='subgenre',
        blank=True
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre', default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'subgenre', 'genre'],
                name='unique_genre_game'
            )
        ]
