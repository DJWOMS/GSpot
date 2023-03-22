from rest_framework import serializers
from .models import models, Language, ProductLanguage, Genre, SubGenre


class LanguageSerializer(serializers.ModelSerializer):
    """Язык"""

    class Meta:
        model = Language
        fields = ('id', 'name')


class ProductLanguageSerializer(serializers.ModelSerializer):
    """Поддерживаемый язык у игры"""
    language_name = serializers.CharField(source='language.name')

    class Meta:
        model = ProductLanguage
        fields = (
            'id',
            'language_name',
            'interface',
            'subtitles',
            'voice'
        )


class GenreSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices='')
    """Жанр для игры"""

    class Meta:
        model = Genre
        fields = ('id', 'name')


class SubGenreSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(read_only=True)
    """Поджанр для игры"""

    class Meta:
        model: SubGenre
        fields = ('id', 'name', 'genre', 'products')
