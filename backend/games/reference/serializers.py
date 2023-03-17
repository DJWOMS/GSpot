<<<<<<< HEAD
from rest_framework import serializers

from .models import Language, ProductLanguage, Group, GroupElement


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


class GroupSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices='')

    class Meta:
        model = Group
        fields = ('id', 'name', 'type')


class GroupElementSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model: GroupElement
        fields = ('id', 'name', 'group')
=======
from rest_framework import serializers
from games.reference.models import Genre, SubGenre


class GenreSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices='')

    class Meta:
        model = Genre
        fields = ('id', 'name')


class SubGenreSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model: SubGenre
        fields = ('id', 'name', 'genre', 'products')
>>>>>>> 2c402bf (исправлены модели и названия классов в соответсвии с моделями   файлах в views,admin,serializers)
