from django.db import models
from core.models import Product


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


class Social(models.Model):
    class SocialTypes(models.TextChoices):
        FACEBOOK = 'FB', 'FaceBook'
        VKONTAKTE = 'VK', 'VKontakte'
        SITE = 'S', 'Site'
        YOUTUBE = 'YT', 'YouTube'
        TWITTER = 'TW', 'Twitter'
        TWITCH = 'TV', 'Twitch'
        TELEGRAM = 'TG', 'Telegram'

    type = models.CharField(
        'Социальная сеть',
        max_length=20,
        choices=SocialTypes.choices,
        default=SocialTypes.SITE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_socials',
        limit_choices_to={'type': Product.TypeProduct.GAMES}
    )
    url = models.URLField('Ссылка')

    def __str__(self):
        return f'{self.type} {self.product.name}'

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
