from rest_framework import serializers
from . import models


class LanguageSerializer(serializers.ModelSerializer):
    """Язык"""

    class Meta:
        model = models.Language
        fields = ('id', 'name')


class ProductLanguageSerializer(serializers.ModelSerializer):
    """Поддерживаемый язык у игры"""
    language_name = serializers.CharField(source='language.name')

    class Meta:
        model = models.ProductLanguage
        fields = (
            'id',
            'language_name',
            'interface',
            'subtitles',
            'voice'
        )
