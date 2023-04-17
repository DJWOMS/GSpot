import uuid
from django.db import models
from base.choices import BaseTextChoices, TypeProductChoices
from base.model_fields import get_field_from_choices
from simple_history.models import HistoricalRecords


class Product(models.Model):
    class StatusProductChoices(BaseTextChoices):
        MODERATION = 'MODERATION', 'Moderation'
        PUBLISH = 'PUBLISH', 'Publish'
        CLOSE = 'CLOSE', 'Close'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True, db_index=True)
    developers_uuid = models.UUIDField(db_index=True)
    publishers_uuid = models.UUIDField(db_index=True)
    description = models.TextField()
    about = models.TextField()
    age = models.IntegerField(blank=True, null=True)
    adult = models.TextField(blank=True, null=True)
    status = get_field_from_choices(
        'Status product', StatusProductChoices, default=StatusProductChoices.MODERATION
    )
    type = get_field_from_choices('Type product', TypeProductChoices)
    dlcs = models.ManyToManyField('self', through="GameDlcLink", blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class GameDlcLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='dlc_link',
        limit_choices_to={'type': TypeProductChoices.GAMES}
    )
    dlc = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='game_link',
        limit_choices_to={'type': TypeProductChoices.DLC}
    )

    class Meta:
        db_table = 'game_dlc_link'
        constraints = [
            models.UniqueConstraint(
                fields=['dlc'],
                name='unique_dlc_game'
            )
        ]
