from rest_framework import serializers

from django.db.models import Min, Max

from finance.models.offer import Price

from reference.models.genres import SubGenre


class MinMaxPriceSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()

    def get_min_price(self, obj):
        return Price.objects.aggregate(Min("amount")).get("amount__min")

    def get_max_price(self, obj):
        return Price.objects.aggregate(Max("amount")).get("amount__max")

    class Meta:
        model = Price
        fields = ("min_price", "max_price")


class GenreSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = ('id', 'name', 'genre')
