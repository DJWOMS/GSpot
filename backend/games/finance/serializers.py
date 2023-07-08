from rest_framework import serializers
from django.db.models import Count
from django.db import transaction
from core.models.product import Product
from finance.models import Price, ProductOffer, Offer, Library


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    price = PriceSerializer()
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Offer
        fields = ('id', 'created_by', 'is_active', 'products', 'price')

    @transaction.atomic
    def create(self, validated_data):
        products_data = validated_data.pop('products')
        developer = set()
        for product in products_data:
            developer.add(product.developers_uuid)
            if len(developer) > 1:
                raise serializers.ValidationError(
                    {"mesage": 'Нельзя создать пакет с разными разработчиками'}
                )
        price_date = validated_data.pop('price')
        price = Price.objects.create(**price_date)
        offer = Offer.objects.create(**validated_data, price=price)
        product_offer = [
            ProductOffer(
                offer=offer,
                product=product,
                created_by=product.developers_uuid
            ) for product in products_data
        ]
        ProductOffer.objects.bulk_create(product_offer)
        return offer


class OfferPriceSerializer(serializers.ModelSerializer):
    price = PriceSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class ProductOfferSerializer(serializers.ModelSerializer):
    offer = OfferPriceSerializer()

    class Meta:
        model = ProductOffer
        exclude = ('product',)


class ProductLibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'developers_uuid',
            'publishers_uuid',
        )


class LibrarySerializer(serializers.ModelSerializer):
    products = ProductLibrarySerializer(many=True)

    class Meta:
        model = Library
        fields = ('products',)


class ProductPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name',)


class PricePackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('amount', 'currency',)


class OfferPackSerializer(serializers.ModelSerializer):
    price = PricePackSerializer()
    products = ProductPackSerializer(many=True)

    class Meta:
        model = Offer
        fields = ('id', 'price', 'products',)


class DlcsPackSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        try:
            offer = ProductOffer.objects.annotate(
                product_count=Count('product')).filter(product=obj, product_count=1)[0].offer
        except ProductOffer.DoesNotExist:
            return None
        return [offer.price.amount, offer.price.currency]

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', )


class ProductContentShowSerializer(serializers.ModelSerializer):
    offers = OfferPackSerializer(many=True)
    dlcs = DlcsPackSerializer(many=True)

    class Meta:
        model = Product
        fields = ('offers', 'dlcs',)
