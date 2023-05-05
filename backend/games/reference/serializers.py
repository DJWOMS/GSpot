from rest_framework import serializers

from .models import Language, ProductLanguage, Genre, SubGenre


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class ProductLanguageSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Genre
        exclude = ('products',)


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = ('id', 'name')


class GenreGamesSerializer(serializers.ModelSerializer):
    subgenres = SubGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'subgenres')
