from rest_framework import serializers
from .models import Language, ProductLanguage, Genre, SubGenre


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


class SubGenreSerializer(serializers.ModelSerializer):
    """Поджанры"""

    class Meta:
        model = SubGenre
        fields = ('id', 'name')


class GenreSerializer(serializers.ModelSerializer):
    """Жанры"""

    subgenres = SubGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'subgenres')


class GenersGameSerializer(serializers.ModelSerializer):
    """Жанр игры"""

    genre = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SubGenre
        fields = 'genre'
