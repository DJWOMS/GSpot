from django.db import models
from core.models import Product


class Language(models.Model):
    name = models.CharField(
        'Наименование языка',
        max_length=100,
        help_text='Введите наименование языка'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class ProductLanguage(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='game_supported_language'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='langs',
    )
    interface = models.BooleanField(verbose_name='Интерфейс', default=True)
    subtitles = models.BooleanField(verbose_name='Титры', default=True)
    voice = models.BooleanField(verbose_name='Озвучка', default=True)

    def __str__(self):
        return self.language.name + "|" + self.product.name

    class Meta:
        verbose_name = 'Поддерживаемый язык'
        verbose_name_plural = 'Поддерживаемые языки'
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'product'],
                name='unique_language_game'
            )
        ]


class Genre(models.Model):
    name = models.CharField('Genre', max_length=50, unique=True, db_index=True)
    products = models.ManyToManyField(Product, related_name='genres', through='GenreProduct')

    def __str__(self):
        return self.name


class SubGenre(models.Model):
    name = models.CharField('Subgenre', max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='subgenres')
    products = models.ManyToManyField(Product, related_name='subgenres', through='SubgenreProduct')

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)


class GenreProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
