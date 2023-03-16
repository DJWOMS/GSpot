from rest_framework import serializers

from .models import Product, GameDlcLink, SystemRequirement

class DlcSerializer(serializers.ModelSerializer):
    """ Детали DLC """
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'developers_uuid',
                  'publishers_uuid',
                  )

class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """
    dlcs = DlcSerializer(many=True, read_only=True)

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
            'dlcs'
        )

class DlcListSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    class Meta:
        model = Product
        fields = ('id', 'name', 'description',)

class SystemRequirementSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    class Meta:
        model = SystemRequirement
        fields = '__all__'
