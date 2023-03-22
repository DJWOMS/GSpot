from django.db import models

class Media(models.Model):
    GAME_LOGO = 'logo'
    PHOTO_SLIDER = 'slider'
    MEDIA_CHOICES = [
        (GAME_LOGO, 'Game Logo'),
        (PHOTO_SLIDER, 'Photo Slider'),
    ]

    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=255)
    file_link = models.FileField(upload_to='product_media', default='test')
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=MEDIA_CHOICES, max_length=10)

    def __str__(self):
        return self.product_id
    class Meta:
        verbose_name_plural = 'Медиа'
