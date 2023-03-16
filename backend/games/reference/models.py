from django.db import models
import uuid

from core.models import Product

class Ganre(models.Model):
    name = models.CharField('категории', max_length=50, db_index=True)
    
    def __str__(self) -> str:
        return self.name


    class Meta():
        verbose_name = 'категория для жанра'
        verbose_name_plural = 'категории для жанров'
        

class SubGanre(models.Model):
    name = models.CharField('sub ganre', max_length=50)
    ganre_id = models.ForeignKey(Ganre, related_name='ganre', unique=True, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product, related_name='sub_ganre')
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta():
        verbose_name = 'жанр для игры'
        verbose_name_plural = 'жанры для игр'

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
