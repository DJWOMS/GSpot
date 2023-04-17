from django.db import models
from core.models import Product


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'


class ProductLanguage(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='games'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='langs',
    )
    interface = models.BooleanField(default=True)
    subtitles = models.BooleanField(default=True)
    voice = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_language'
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'product'],
                name='unique_language_game'
            )
        ]
