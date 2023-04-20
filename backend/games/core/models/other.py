import uuid
from django.db import models
from base.model_fields import get_field_from_choices

from .product import Product
from base.choices import BaseTextChoices, TypeProductChoices
from simple_history.models import HistoricalRecords


class SystemRequirement(models.Model):
    class OSChoices(BaseTextChoices):
        LINUX = 'LINUX', 'Linux'
        WINDOWS = 'WINDOWS', 'Windows'
        MACOS = 'MACOS', 'MacOS'
        PS = 'PS', 'PlayStation'
        XBOX = 'XBOX', 'XBox'

    class TypeRequirementsChoices(BaseTextChoices):
        MINIMUM = 'MINIMUM', 'Minimals'
        RECOMMEND = 'RECOMMEND', 'Recommends'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operating_system = get_field_from_choices('Operation system', OSChoices)
    game = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='system_requirements',
        limit_choices_to={'type': TypeProductChoices.GAMES}
    )
    device_processor = models.CharField('Processor', max_length=100)
    device_memory = models.CharField('Memory', max_length=100)
    device_storage = models.CharField('Storage', max_length=100)
    device_graphics = models.CharField('Graphics', max_length=100)
    type_requirements = get_field_from_choices('System requirement', TypeRequirementsChoices)
    history = HistoricalRecords()

    def __str__(self):
        return self.type_requirements

    class Meta:
        db_table = 'system_requirement'
