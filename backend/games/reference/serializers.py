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

    def to_representation(self, instance):
        # Get subgenres from context
        subgenres = self.context.get('subgenres', [])

        # Filter subgenres that belong to the current instance
        subgenres = [subgenre for subgenre in subgenres if subgenre.genre_id == instance.genre_id]

        # Serialize subgenres and add them to the representation
        data = super().to_representation(instance)
        data['subgenres'] = SubGenreSerializer(subgenres, many=True).data
        return data


class GenreGamesSerializer(serializers.ModelSerializer):
    subgenres = SubGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'subgenres')
