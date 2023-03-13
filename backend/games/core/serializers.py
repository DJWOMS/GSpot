from rest_framework import serializers

from .models import Product, GameDlcLink, SystemRequirement


class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'developers_uuid',
            'publishers_uuid',
            'release_date',
            'description',
            'about',
            'age',
            'adult',
            'status',
            'type'
        )


class ProductListSerializer(serializers.ModelSerializer):
    """ Список игр """

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
            'type'
        )


class DlcSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    class Meta:
        model = GameDlcLink
        fields = ('id', 'game_id', 'dls_id')
