from rest_framework.serializers import ModelSerializer

from base.models import BasePermission, BaseGroup


class BasePermissionSerializer(ModelSerializer):
    class Meta:
        model = BasePermission
        fields = ['name', 'codename']
        abstract = True


class BaseGroupSerializer(ModelSerializer):
    class Meta:
        model = BaseGroup
        fields = ['name', 'permission']
        abstract = True
