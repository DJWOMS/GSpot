from rest_framework import serializers

from .models import Product, GameDlcLink, SystemRequirement


class GameDlcLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameDlcLink
        fields = ('id',
                  'game',
                  'dlc'
                  )
class DlcSerializer(serializers.ModelSerializer):
    """ Детали DLC """
    games = GameDlcLinkSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'developers_uuid',
                  'publishers_uuid',
                  'games',
                  )

class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """
    dlc = GameDlcLinkSerializer(many=True, read_only=True)

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
            'dlc'
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
