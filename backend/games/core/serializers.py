from rest_framework import serializers

from finance.serializers import OfferSerializer, PriceSerializer
from reference import serializers as ref_serializers
from community import serializers as com_serializers
from reference.serializers import GenreGamesSerializer
from .models import SystemRequirement, Product


class DlcSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = SystemRequirement
        exclude = ('game',)


class OperatingSystemSerializer(serializers.Serializer):
    """ Operating System Serializer """

    class Meta:
        model = SystemRequirement
        fields = ('operating_system',)


class ProductSerializer(serializers.ModelSerializer):
    dlcs = DlcSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    system_requirements = SystemRequirementSerializer(many=True, read_only=False)
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
            'system_requirements',
            'socials',
        )


class ShortSystemReqSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemRequirement
        fields = ('id', 'operating_system')


class GamesListSerializer(serializers.ModelSerializer):
    # todo реализовать прайс
    # price = serializers.IntegerField(default=100)
    # todo реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # todo продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = ShortSystemReqSerializers(many=True, read_only=True)
    genres = GenreGamesSerializer(many=True, read_only=True)
    offers = OfferSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'genres',
            'system_requirements',
            'price',
            'discount',
            'is_bought',
            'is_favorite',
            'offers',
        )


class GameDetailSerializer(serializers.ModelSerializer):
    # todo реализовать прайс
    # price = serializers.IntegerField(default=100)
    # todo реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # todo продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = SystemRequirementSerializer(many=True, read_only=True)
    genres = GenreGamesSerializer(many=True, read_only=True)
    dlcs = DlcSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    offers = OfferSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'release_date',
            'genres',
            'price',
            'discount',
            'is_bought',
            'is_favorite',
            'description',
            'about',
            'age',
            'adult',
            'adult',
            'status',
            'type',
            'developers_uuid',
            'publishers_uuid',
            'dlcs',
            'langs',
            'system_requirements',
            'offers',
        )
