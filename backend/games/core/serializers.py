from rest_framework import serializers
from .models import Product


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
