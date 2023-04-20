from django.db import models
from core.models import Product
import uuid
from reference.models import Language


GRADE_CHOICES = (
    ('Like', 'Like'),
    ('Dislike', 'Dislike'),
)


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
        db_table = 'media'


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
        max_length=20,
        choices=SocialTypes.choices,
        default=SocialTypes.SITE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='socials',
        limit_choices_to={'type': Product.TypeProduct.GAMES}
    )
    url = models.URLField()

    def __str__(self):
        return f'{self.type} {self.product.name}'

    class Meta:
        db_table = 'social'


class Review(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    game = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    grade = models.CharField(choices=GRADE_CHOICES, max_length=10)
    view_type = models.BooleanField(default=True)
    can_reply = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review {self.game}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Comment(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'Comment {self.id}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Reaction(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_type = models.CharField(choices=GRADE_CHOICES, max_length=10)

    def __str__(self):
        return f'{self.like_type} for Review {self.review_id}'

    class Meta:
        verbose_name = 'Like/Dislike'
        verbose_name_plural = 'Likes/Dislikes'
