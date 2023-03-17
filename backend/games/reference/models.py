from django.db import models

from core.models import Product


class Genre(models.Model):
    name = models.CharField('жанр продукта', max_length=50, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta():
        verbose_name = 'жанр продукта'
        verbose_name_plural = 'жанры для продуктов'


class SubGenre(models.Model):
    name = models.CharField('поджанр для продукта', max_length=50)
    genre_id = models.ForeignKey(
        Genre, related_name='genre', unique=True, on_delete=models.CASCADE
    )
    products_id = models.ManyToManyField(
        Product, related_name='subgenre', through='SubgenreProduct'
    )

    def __str__(self) -> str:
        return self.name

    class Meta():
        verbose_name = 'поджанр для продукта'
        verbose_name_plural = 'поджанр для продуктов'


class Language(models.Model):
    name = models.CharField('Наименование языка',
                            max_length=100,
                            help_text='Введите наименование языка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class ProductLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                 related_name='game_supported_language')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='languages')
    interface = models.BooleanField(verbose_name='Интерфейс', default=True)
    subtitles = models.BooleanField(verbose_name='Титры', default=True)
    voice = models.BooleanField(verbose_name='Озвучка', default=True)

    def __str__(self):
        return self.language.name + "|" + self.product.name

    class Meta:
        verbose_name = 'Поддерживаемый язык'
        verbose_name_plural = 'Поддерживаемые языки'


class SubgenreProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    subgenre_id = models.ForeignKey(SubGenre, on_delete=models.CASCADE)
