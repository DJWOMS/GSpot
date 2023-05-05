from django.db import transaction

from rest_framework import serializers
from community.models import Social
from finance.models.offer import Offer, Price, ProductOffer
from finance.serializers import PriceSerializer, ProductOfferSerializer

from reference import serializers as ref_serializers
from community import serializers as com_serializers
from reference.models.genres import Genre, GenreProduct
from reference.models.langs import Language, ProductLanguage
from reference.serializers import GenreGamesSerializer, GenreSerializer, SubGenreSerializer
from .models import SystemRequirement, Product


class SystemRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemRequirement
        exclude = ('game',)


class ProductSerializer(serializers.ModelSerializer):
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


class CreateProductSerializer(serializers.ModelSerializer):
    system_requirements = SystemRequirementSerializer(many=True)
    langs = ref_serializers.ProductLanguageSerializer(many=True)
    socials = com_serializers.GameSocialSerializer(many=True, required=False)
    product_offer = ProductOfferSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'developers_uuid',
            'publishers_uuid',
            'description',
            'about',
            'age',
            'adult',
            'type',
            'system_requirements',
            'langs',
            'socials',
            'product_offer',
        )

    @transaction.atomic
    def create(self, validated_data):
        system_requirements = validated_data.pop('system_requirements', [])
        langs = validated_data.pop('langs', [])
        socials = validated_data.pop('socials', [])
        product_offer = validated_data.pop('product_offer', None)

        product = Product.objects.create(**validated_data)

        social_objects = [
            Social(product=product, **social) for social in socials
        ]
        Social.objects.bulk_create(social_objects)

        requirement_objects = [
            SystemRequirement(game=product, **requirement) for requirement in system_requirements
        ]
        SystemRequirement.objects.bulk_create(requirement_objects)

        language_objects = [
            ProductLanguage(
                product=product,
                language=Language.objects.get(name=lang['language']['name']),
                interface=lang['interface'],
                subtitles=lang['subtitles'],
                voice=lang['voice']
            ) for lang in langs
        ]
        ProductLanguage.objects.bulk_create(language_objects)

        if product_offer:
            offer_data = product_offer.pop('offer')
            price_data = offer_data.pop('price')
            price = Price.objects.create(**price_data)
            offer = Offer.objects.create(price=price, **offer_data)
            ProductOffer.objects.create(product=product, offer=offer, **product_offer)

        return product


class OperatingSystemSerializer(serializers.Serializer):
    """ Operating System Serializer """

    class Meta:
        model = SystemRequirement
        fields = ('operating_system',)


class ShortSystemReqSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemRequirement
        fields = ('id', 'operating_system')


class GamesListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    # TODO реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # TODO продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = ShortSystemReqSerializers(many=True, read_only=True)
    genres = SubGenreSerializer()

    def get_price(self, obj):
        try:
            offer = ProductOffer.objects.get(product=obj).offer
        except ProductOffer.DoesNotExist:
            return None
        return offer.price.amount

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
            'is_favorite'
        )


class GameDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    # TODO реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # TODO продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = SystemRequirementSerializer(many=True, read_only=True)
    genres = GenreGamesSerializer(many=True, read_only=True)
    dlcs = ProductSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    genres = GenreGamesSerializer(many=True, read_only=True)

    def get_price(self, obj):
        try:
            offer = ProductOffer.objects.get(product=obj).offer
        except ProductOffer.DoesNotExist:
            return None
        return offer.price.amount

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
        )
