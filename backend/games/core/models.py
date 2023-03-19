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

    id = models.UUIDField('UUID продукта', primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Идентификатор записи ')

    name = models.CharField(
        'Наименование продукта',
        max_length=100,
        help_text='Введите наименование продукта'
    )

    release_date = models.DateField(
        'Дата релиза',
        auto_now_add=True,
        db_index=True
    )

    developers_uuid = models.UUIDField(
        'UUID разработчика - service Users',
        db_index=True
    )

    publishers_uuid = models.UUIDField(
        'UUID издателя - service Users',
        db_index=True
    )

    description = models.TextField(
        'Краткое описание',
        help_text='Укажите краткое описание'
    )

    about = models.TextField(
        'Об этой игре / информация о дополнении',
        help_text='Укажите описание'
    )

    age = models.IntegerField(
        'Возрастное ограничение',
        blank=True,
        null=True
    )

    adult = models.TextField(
        'Описание возрастного ограничения',
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=2,
        choices=StatusProduct.choices,
        default=StatusProduct.MODERATION
    )

    type = models.CharField(
        max_length=2,
        choices=TypeProduct.choices,
        help_text='Укажите тип продукта'
    )

    dlcs = models.ManyToManyField(
        'self', through="GameDlcLink", blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'товары'


class GameDlcLink(models.Model):
    id = models.UUIDField(
        'UUID продукта',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    game = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='dlc_link',
        limit_choices_to={'type': Product.TypeProduct.GAMES}
    )

    dlc = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='game_link',
        limit_choices_to={'type': Product.TypeProduct.DLC}
    )

    class Meta:
        db_table = 'game_dlc_link'
        verbose_name = 'дополнение для игры'
        verbose_name_plural = 'дополнение для игры'
        constraints = [
            models.UniqueConstraint(
                fields=['dlc_id'],
                name='unique_subscriber'
            )
        ]


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

    id = models.UUIDField(
        'UUID продукта',
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    operating_system = models.CharField(
        'ОС',
        max_length=2,
        choices=OS.choices,
        help_text='Укажите ОС'
    )

    game = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='system_requirements',
        limit_choices_to={
            'type': Product.TypeProduct.GAMES}
    )

    device_processor = models.CharField(
        'Процессор',
        max_length=100,
        help_text='Укажите процессор'
    )

    device_memory = models.CharField(
        'Количество ОЗУ',
        max_length=100,
        help_text='Укажите количество ОЗУ'
    )

    device_storage = models.CharField(
        'Количество памяти на Диске',
        max_length=100,
        help_text='Укажите количество памяти на Диске'
    )

    device_graphics = models.CharField(
        'Модель видеокарты и количество памяти',
        max_length=100,
        help_text='Укажите модель видеокарты и количество памяти')

    type_requirements = models.CharField(
        'Тип системных требований',
        max_length=2,
        choices=TypeRequirements.choices,
        help_text='Укажите тип системных требований'
    )

    def __str__(self):
        return self.type_requirements

    class Meta:
        db_table = 'system_requirement'
        verbose_name = 'системная характеристика'
        verbose_name_plural = 'системные характеристики'
