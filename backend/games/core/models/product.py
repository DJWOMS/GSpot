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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True, db_index=True)
    developers_uuid = models.UUIDField(db_index=True)
    publishers_uuid = models.UUIDField(db_index=True)
    description = models.TextField()
    about = models.TextField()
    age = models.IntegerField(blank=True, null=True)
    adult = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=StatusProduct.choices,
        default=StatusProduct.MODERATION
    )
    type = models.CharField(max_length=2, choices=TypeProduct.choices)
    dlcs = models.ManyToManyField('self', through="GameDlcLink", blank=True)

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
        constraints = [
            models.UniqueConstraint(
                fields=['dlc'],
                name='unique_dlc_game'
            )
        ]
