from django.db import models
from core.models import Product
import uuid
from reference.models import Language


class Media(models.Model):
    GAME_LOGO = 'logo'
    PHOTO_SLIDER = 'slider'
    MEDIA_CHOICES = [
        (GAME_LOGO, 'Game Logo'),
        (PHOTO_SLIDER, 'Photo Slider'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_link = models.FileField(upload_to='product_media')
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=MEDIA_CHOICES, max_length=10)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class Reviews(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    game = models.CharField(max_length=255)
    text = models.TextField()
    grade = models.DecimalField(max_digits=3, decimal_places=1)
    view_type = models.CharField(max_length=50)
    can_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review {self.game}'

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
