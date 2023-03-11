import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class StatusProduct(models.TextChoices):
        MODERATION = 'M', _('MODERATION')
        PUBLISH = 'P', _('PUBLISH')
        CLOSE = 'C', _('CLOSE')

    class TypeProduct(models.TextChoices):
        GAMES = 'G', _('GAMES')
        DLC = 'D', _('ADDITIONS')

    id = models.UUIDField('UUID продукта',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    name = models.CharField('Наименование продукта',
                            max_length=100,
                            help_text='Введите наименование продукта')

    release_date = models.DateField('Дата релиза',
                                    auto_now_add=True,
                                    db_index=True)

    developers_uuid = models.UUIDField('UUID разработчика - service Users',
                                       db_index=True)

    publishers_uuid = models.UUIDField('UUID издателя - service Users',
                                       db_index=True)

    description = models.TextField('Краткое описание',
                                   help_text='Укажите краткое описание')

    about = models.TextField('Об этой игре / информация о дополнении',
                             help_text='Укажите описание')

    age = models.IntegerField('Возрастное ограничение',
                              blank=True,
                              null=True)

    adult = models.TextField('Описание возрастного ограничения',
                             blank=True,
                             null=True,)

    status = models.CharField(max_length=2,
                              choices=StatusProduct.choices,
                              default=StatusProduct.MODERATION)

    type = models.CharField(max_length=2,
                            choices=TypeProduct.choices,
                            help_text='Укажите тип продукта')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'товары'
