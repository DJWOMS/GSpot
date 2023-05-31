from rest_framework import serializers, exceptions
from core.models.product import Product
from finance.models import Price, ProductOffer, Offer, Cart, CartOffer, Library
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


class OfferInCartSerializerCreate(serializers.Serializer):
    offers = serializers.PrimaryKeyRelatedField(many=False, queryset=Offer.objects.all())
    created_by = serializers.UUIDField()
    gift_recipient = serializers.UUIDField()

    def validate(self, data):
        created_by = data.get('created_by')
        gift_recipient = data.get('gift_recipient')
        offers = data.get('offers')
        if offers.products.count() <= 1:
            raise serializers.ValidationError('Оффер должен быть связан более чем с одной игрой')
        if Cart.objects.filter(
            created_by=created_by, gift_recipient=gift_recipient, offers=offers
        ).exists():
            raise serializers.ValidationError('Такой продукт уже есть в корзине')
        return data

    @transaction.atomic
    def create(self, validated_data):
        offer = validated_data.pop('offers')
        created_by = validated_data.pop('created_by')
        gift_recipient = validated_data.pop('gift_recipient')
        if not Cart.objects.filter(created_by=created_by).exists():
            cart = Cart.objects.create(created_by=created_by, gift_recipient=gift_recipient)
        else:
            cart = Cart.objects.get(created_by=created_by)
            if cart.gift_recipient != gift_recipient:
                raise exceptions.ValidationError(
                    'В корзину уже добавлены игры либо для себя либо для подарка, '
                    'нельзя добавлять и для себя и в подарок одновременно'
                )
        cart_offer = CartOffer.objects.create(offer=offer, cart=cart)
        return cart_offer
