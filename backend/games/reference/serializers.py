from rest_framework import serializers
from .models import Language, ProductLanguage, Genre, SubGenre
# from core.serializers import ProductSerializer
from rest_framework.validators import UniqueTogetherValidator


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
    """Жанр для игры"""

    class Meta:
        model = Genre
        fields = ('id', 'name')


class SubGenreSerializer(serializers.ModelSerializer):
    """Поджанр для игры"""
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    # products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubGenre
        fields = ('id', 'name', 'genre')
        validators = [
            UniqueTogetherValidator(
                queryset=SubGenre.objects.all(),
                fields=['name', 'genre']
            )
        ]
