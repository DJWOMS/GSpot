from rest_framework import serializers
from core.models.product import Product
from finance.models import Price, ProductOffer, Offer, Cart, CartOffer
from django.db import transaction


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


class ProductOfferSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()

    class Meta:
        model = ProductOffer
        exclude = ('product',)


class CartSerializerCreate(serializers.ModelSerializer):
    offers = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all())

    class Meta:
        model = Cart
        fields = ('created_by', 'gift_recipient', 'offers')

    @transaction.atomic
    def create(self, validated_data):
        offer = validated_data.pop('offers')
        created_by = validated_data.pop('created_by')
        gift_recipient = None
        if self.initial_data.get('gift_recipient'):
            gift_recipient = validated_data.pop('gift_recipient')
        cart = Cart.objects.create(created_by=created_by, gift_recipient=gift_recipient)
        CartOffer.objects.create(offer=offer[0], cart=cart)
        return cart
