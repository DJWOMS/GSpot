from rest_framework import serializers
from .models import Language, ProductLanguage, Genre, SubGenre


class LanguageSerializer(serializers.ModelSerializer):
    """Язык"""

    class Meta:
        model = Language
        fields = ('id', 'name',)


class ProductLanguageSerializer(serializers.ModelSerializer):
    """Поддерживаемый язык у игры"""

    class Meta:
        model = ProductLanguage
        fields = (
            'id', 'language', 'product', 'interface', 'subtitles', 'voice'
        )


class GenreSerializer(serializers.ModelSerializer):
    """жанр для игры"""

    class Meta:
        model = Genre
        fields = ('id', 'name', 'genre')


class SubGenreSerializer(serializers.ModelSerializer):
    """поджанр для игры"""

    class Meta:
        model: SubGenre
        fields = ('id', 'name', 'genre_id', 'products_id')
