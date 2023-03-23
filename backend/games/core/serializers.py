from rest_framework import serializers

from reference import serializers as ref_serializers
from reference.serializers import GenersGameSerializer
from .models import SystemRequirement, Product


class SystemRequirementSerializer(serializers.ModelSerializer):
    """ Системные требования """

    class Meta:
        model = SystemRequirement
        exclude = ('game',)


class ShortSystemReqSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemRequirement
        fields = ('id', 'operating_system')


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


class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """
    dlcs = DlcSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    system_requirements = SystemRequirementSerializer(many=True, read_only=False)

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
            'system_requirements'
        )


class DlcListSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    class Meta:
        model = Product
        fields = ('id', 'name', 'description',)


class GamesListSerializer(serializers.ModelSerializer):
    # price = 100
    # discount = 0
    # isBought = 'false'
    # isFavorite = 'false'
    systemRequirements = ShortSystemReqSerializers(many=True, read_only=True)
    genres = GenersGameSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'genres',
            'systemRequirements',
            # 'price',
            # 'discount',
            # 'isBought',
            # 'isFavorite'
        )
