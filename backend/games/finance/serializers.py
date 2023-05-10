from rest_framework import serializers

from .models.offer import Offer, Price, ProductOffer


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    price = PriceSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class ProductOfferSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()

    class Meta:
        model = ProductOffer
        exclude = ('product',)
