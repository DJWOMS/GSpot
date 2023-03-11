import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from .product import Product


class SystemRequirement(models.Model):
    class OS(models.TextChoices):
        LINUX = 'L', _('Linux')
        WINDOWS = 'W', _('Windows')
        MACOS = 'M', _('MacOS')
        PS = 'P', _('PlayStation')
        XBOX = 'X', _('XBox')

    class TypeRequirements(models.TextChoices):
        MINIMUM = 'M', _('Minimals')
        RECOMMEND = 'R', _('Recommends')



    id = models.UUIDField('UUID продукта',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    operating_system = models.CharField('ОС',
                                        max_length=2,
                                        choices=OS.choices,
                                        help_text='Укажите ОС')

    game_id = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='system_requirements',
                                limit_choices_to={'type':Product.TypeProduct.GAMES})

    device_processor = models.CharField('Процессор',
                                        max_length=100,
                                        help_text='Укажите процессор')

    device_memory = models.CharField('Колличество ОЗУ',
                                     max_length=100,
                                     help_text='Укажите колличество ОЗУ')

    device_storage = models.CharField('Колличество памяти на Диске',
                                      max_length=100,
                                      help_text='Укажите колличество памяти на Диске')

    device_graphics = models.CharField('Модель видеокарты и колличество памяти',
                                       max_length=100,
                                       help_text='Укажиет модель видеокарты и колличество памяти')

    type_requirements = models.CharField('Тип системных требований',
                                         max_length=2,
                                         choices=TypeRequirements.choices,
                                         help_text='Укажите тип системных требований')

    def __str__(self):
        return self.type_requirements

    class Meta:
        db_table = 'system_requirement'
        verbose_name = 'системная характеристика'
        verbose_name_plural = 'системные характеристики'
