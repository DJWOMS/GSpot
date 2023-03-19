from rest_framework import serializers

from reference import serializers as ref_serializers
from . import models


class SystemRequirementSerializer(serializers.ModelSerializer):
    """ Системные требования """

    class Meta:
        model = models.SystemRequirement
        exclude = ('game',)


class DlcSerializer(serializers.ModelSerializer):
    """ Детали DLC """
    langs = ref_serializers.ProductLanguageSerializer(many=True)

    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'description',
            'developers_uuid',
            'publishers_uuid',
            'langs',
        )


class ProductSerializer(serializers.ModelSerializer):
    """ Продукт """
    dlcs = DlcSerializer(many=True, read_only=False)
    langs = ref_serializers.ProductLanguageSerializer(many=True, read_only=False)
    system_requirements = SystemRequirementSerializer(many=True, read_only=False)

    class Meta:
        model = models.Product
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
            'dlcs',
            'langs',
            'system_requirements'
        )


class DlcListSerializer(serializers.ModelSerializer):
    """ Детали DLC """

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description',)
