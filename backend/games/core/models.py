import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Social(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField('Наименования соц. сети'
                            ,max_length=100)

class Product(models.Model):
    class StatusProduct(models.TextChoices):
        MODERATION = 'M', _('MODERATION')
        PUBLISH = 'P', _('PUBLISH')
        CLOSE = 'C', _('CLOSE')

    id = models.UUIDField('UUID продукта'
                          ,primary_key=True
                          ,default = uuid.uuid4
                          ,editable = False)
    name = models.CharField('Наименование продукта'
                            ,max_length=100
                            ,help_text='Введите наименование продукта')
    release_date = models.DateField('Дата релиза'
                                    ,auto_now_add=True
                                    ,db_index=True)
    developers_uuid = models.UUIDField('UUID разработчика - service Users'
                                       ,db_index=True)
    publishers_uuid = models.UUIDField('UUID издателя - service Users'
                                       ,db_index=True)
    description = models.TextField('Описание продукта')
    about = models.TextField('Описание продукта')
    age = models.CharField('Возрастное ограничение'
                           ,max_length=10)
    adult = models.TextField
    status = models.CharField(
        max_length=2,
        choices=StatusProduct.choices,
        default=StatusProduct.MODERATION,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'товары'
