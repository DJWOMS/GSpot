from django.db import transaction

from rest_framework import serializers
from community.models import Social
from core.models.product import GameDlcLink
from finance.models.offer import Offer, Price, ProductOffer
from finance.serializers import ProductOfferSerializer
from finance.mixins import PricePackSeriazerMixin

from reference import serializers as ref_serializers
from community import serializers as com_serializers
from reference.models.genres import Genre, GenreProduct
from reference.models.langs import Language, ProductLanguage
from reference.serializers import GenreGamesSerializer
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
    product_offer = ProductOfferSerializer(write_only=True)
    genres = serializers.ListField(child=serializers.CharField(), write_only=True)

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
            'genres',
        )

    @transaction.atomic
    def create(self, validated_data):
        system_requirements = validated_data.pop('system_requirements', None)
        langs = validated_data.pop('langs', None)
        socials = validated_data.pop('socials', None)
        product_offer = validated_data.pop('product_offer', None)
        genres = validated_data.pop('genres', None)

        offer_data = product_offer.pop('offer')
        price_data = offer_data.pop('price')

        price = Price.objects.create(**price_data)
        offer = Offer.objects.create(price=price, **offer_data)
        product = Product.objects.create(**validated_data)
        ProductOffer.objects.create(product=product, offer=offer, **product_offer)

        social_objects = [Social(product=product, **social) for social in socials]
        Social.objects.bulk_create(social_objects)

        requirement_objects = [
            SystemRequirement(game=product, **requirement) for requirement in system_requirements
        ]
        SystemRequirement.objects.bulk_create(requirement_objects)

        language_objects = []
        for lang in langs:
            language_name = lang['language']['name']
            try:
                language = Language.objects.get(name=language_name)
            except Language.DoesNotExist as e:
                raise serializers.ValidationError(str(e), code='invalid')
            language_objects.append(
                ProductLanguage(
                    product=product,
                    language=language,
                    interface=lang['interface'],
                    subtitles=lang['subtitles'],
                    voice=lang['voice'],
                ),
            )

        ProductLanguage.objects.bulk_create(language_objects)

        genre_objects = []
        for genre_name in genres:
            try:
                genre = Genre.objects.get(name=genre_name)
            except Genre.DoesNotExist as e:
                raise serializers.ValidationError(str(e), code='invalid')
            genre_objects.append(GenreProduct(product=product, genre=genre))

        GenreProduct.objects.bulk_create(genre_objects)

        return product


class OperatingSystemSerializer(serializers.Serializer):
    """Operating System Serializer"""

    class Meta:
        model = SystemRequirement
        fields = ('operating_system',)


class ShortSystemReqSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemRequirement
        fields = ('id', 'operating_system')


class GamesListSerializer(serializers.ModelSerializer, PricePackSeriazerMixin):
    price = serializers.SerializerMethodField()
    # TODO реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # TODO продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = ShortSystemReqSerializers(many=True, read_only=True)
    genres = serializers.StringRelatedField(many=True)

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
        )


class PricePackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'amount',
            'currency',
        )


class ProductPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
        )


class OfferPackSerializer(serializers.ModelSerializer):
    price = PricePackSerializer()
    products = ProductPackSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'id',
            'price',
            'products',
        )


class DlcsPackSerializer(serializers.ModelSerializer, PricePackSeriazerMixin):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
        )


class GameDetailSerializer(serializers.ModelSerializer, PricePackSeriazerMixin):
    price = serializers.SerializerMethodField()
    # TODO реализовать систему скидок
    discount = serializers.IntegerField(default=0)
    # TODO продумать систему оценок
    is_bought = serializers.BooleanField(default=False)
    is_favorite = serializers.BooleanField(default=False)

    system_requirements = SystemRequirementSerializer(many=True, read_only=True)
    genres = GenreGamesSerializer(many=True, read_only=True)
    dlcs = DlcsPackSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    genres = GenreGamesSerializer(many=True, read_only=True)
    offers = OfferPackSerializer(many=True)

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
            'offers',
            'dlcs',
            'langs',
            'system_requirements',
        )


class GameDlcLinkSerializer(serializers.Serializer):
    game = serializers.UUIDField()
    dlc = serializers.ListField(child=serializers.UUIDField())

    def create(self, validated_data):
        game_id = validated_data['game']
        dlc_ids = validated_data['dlc']

        dlc_links = []
        for dlc_id in dlc_ids:
            dlc_links.append(GameDlcLink(game_id=game_id, dlc_id=dlc_id))

        GameDlcLink.objects.bulk_create(dlc_links)
        return dlc_links

    def to_representation(self, instance):
        print(instance)
        return {'game': instance[0].game_id, 'dlc': [link.dlc_id for link in instance]}


class SaveToLibrarySerializer(serializers.Serializer):
    user_to = serializers.UUIDField()
    user_from = serializers.UUIDField(required=False)
    offer_uuid = serializers.ListField(child=serializers.UUIDField())
