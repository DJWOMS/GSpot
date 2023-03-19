from rest_framework import serializers
from . import models


class LanguageSerializer(serializers.ModelSerializer):
    """Язык"""

    class Meta:
        model = models.Language
        fields = ('id', 'name')


class ProductLanguageSerializer(serializers.ModelSerializer):
    """Поддерживаемый язык у игры"""

    class Meta:
        model = models.ProductLanguage
        fields = (
            'id',
            'language',
            'product',
            'interface',
            'subtitles',
            'voice'
        )
