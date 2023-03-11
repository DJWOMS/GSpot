import uuid

from django.db import models

from .product import Product


class GameDlcLink(models.Model):
    id = models.UUIDField('UUID продукта',
                               primary_key=True,
                               default=uuid.uuid4,
                               editable=False)

    game_id = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='game_dlc_links',
                                limit_choices_to={'type':Product.TypeProduct.GAMES})

    dls_id = models.ForeignKey(Product,
                               on_delete=models.CASCADE,
                               related_name='dlc_game_links',
                               limit_choices_to={'type':Product.TypeProduct.DLC})

    class Meta:
        db_table='game_dlc_link'
        verbose_name = 'дополнение для игры'
        verbose_name_plural = 'дополнение для игры'
        constraints = [
            models.UniqueConstraint(
                fields=['game_id', 'dls_id'],
                name='unique_subscriber'
            )
        ]
