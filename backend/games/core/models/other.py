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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operating_system = models.CharField(max_length=2, choices=OS.choices)
    game = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='system_requirements',
        limit_choices_to={'type': Product.TypeProduct.GAMES}
    )
    device_processor = models.CharField('Processor', max_length=100)
    device_memory = models.CharField('Memory', max_length=100)
    device_storage = models.CharField('Storage', max_length=100)
    device_graphics = models.CharField('Graphics', max_length=100)
    type_requirements = models.CharField('Min/Rec', max_length=2, choices=TypeRequirements.choices)

    def __str__(self):
        return self.type_requirements

    class Meta:
        db_table = 'system_requirement'
