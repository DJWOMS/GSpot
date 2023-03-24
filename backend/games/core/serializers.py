from rest_framework import serializers

from reference import serializers as ref_serializers
from community import serializers as com_serializers
from reference.serializers import GenreSerializer
from .models import SystemRequirement, Product


class DlcSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    langs = ref_serializers.ProductLanguageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'developers_uuid',
            'publishers_uuid',
            'langs',
        )


class SystemRequirementSerializer(serializers.ModelSerializer):
    """ Системные требования """

    class Meta:
        model = SystemRequirement
        exclude = ('game',)


class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """
    dlcs = DlcSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    systemRequirements = SystemRequirementSerializer(many=True, read_only=False)
    socials = com_serializers.SocialSerializer(many=True, read_only=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'description',
            'about',
            'age',
            'adult',
            'status',
            'type',
            'developers_uuid',
            'publishers_uuid',
            'dlcs',
            'langs',
            'systemRequirements',
            'socials',
        )


class ShortSystemReqSerializers(serializers.ModelSerializer):
    """ Сокращенные системные требования для игры """

    class Meta:
        model = SystemRequirement
        fields = ('id', 'operating_system')


class GamesListSerializer(serializers.ModelSerializer):
    """Лист игр"""

    # todo реализовать прайс
    price = serializers.IntegerField(default=100)
    # todo реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # todo продумать систему оценок
    isBought = serializers.BooleanField(default=False)
    isFavorite = serializers.BooleanField(default=False)

    system_requirements = ShortSystemReqSerializers(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'genre',
            'system_requirements',
            'price',
            'discount',
            'isBought',
            'isFavorite'
        )


class GameDetailSerializer(serializers.ModelSerializer):
    """ Полная информация о игре """

    # todo реализовать прайс
    price = serializers.IntegerField(default=100)
    # todo реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # todo продумать систему оценок
    isBought = serializers.BooleanField(default=False)
    isFavorite = serializers.BooleanField(default=False)

    system_requirements = SystemRequirementSerializer(many=True, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'genre',
            'system_requirements',
            'price',
            'discount',
            'isBought',
            'isFavorite'
        )
