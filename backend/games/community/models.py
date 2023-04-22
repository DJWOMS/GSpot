from django.db import models
from base.model_fields import get_field_from_choices
from core.models import Product
import uuid
from reference.models import Language
from base.choices import BaseTextChoices, GradeChoices, TypeProductChoices
from simple_history.models import HistoricalRecords


class Media(models.Model):
    class MediaFileTypeChoices(BaseTextChoices):
        GAME_LOGO = 'GAME_LOGO', 'Game Logo'
        PHOTO_SLIDER = 'PHOTO_SLIDER', 'Photo Slider'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_link = models.FileField(upload_to='product_media')
    created_at = models.DateTimeField(auto_now_add=True)
    type = get_field_from_choices('Media_file', MediaFileTypeChoices)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.product}'

    class Meta:
        db_table = 'media'


class Social(models.Model):
    class SocialMediaTypesChoices(BaseTextChoices):
        FACEBOOK = 'FACEBOOK', 'FaceBook'
        VKONTAKTE = 'VKONTAKTE', 'VKontakte'
        SITE = 'SITE', 'Site'
        YOUTUBE = 'YOUTUBE', 'YouTube'
        TWITTER = 'TWITTER', 'Twitter'
        TWITCH = 'TWITCH', 'Twitch'
        TELEGRAM = 'TELEGRAM', 'Telegram'

    type = get_field_from_choices(
        'Social_media',
        SocialMediaTypesChoices,
        default=SocialMediaTypesChoices.SITE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='socials',
        limit_choices_to={'type': TypeProductChoices.GAMES}
    )
    url = models.URLField()
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.type} {self.product.name}'

    class Meta:
        db_table = 'social'


class Review(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    game = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    grade = get_field_from_choices('Grade', GradeChoices)
    view_type = models.BooleanField(default=True)
    can_reply = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    history = HistoricalRecords()

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
    history = HistoricalRecords()

    def __str__(self):
        return f'Comment {self.id}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Reaction(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_type = get_field_from_choices('Grade', GradeChoices)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.like_type} for Review {self.review_id}'

    class Meta:
        verbose_name = 'Like/Dislike'
        verbose_name_plural = 'Likes/Dislikes'
