from django.db import models

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