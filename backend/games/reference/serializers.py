from rest_framework import serializers
from .models import Language, ProductLanguage


class LanguageSerializer(serializers.ModelSerializer):
    """Язык"""

    class Meta:
        model = Language
        fields = ('id', 'name',)


class ProductLanguageSerializer(serializers.ModelSerializer):
    """Поддерживаемый язык у игры"""

    class Meta:
        model = ProductLanguage
        fields = ('id', 'language', 'product', 'interface', 'subtitles', 'voice')
