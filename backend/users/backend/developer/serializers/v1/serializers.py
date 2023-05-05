from developer.models import DeveloperPermission, DeveloperGroup

from base.serializers import BasePermissionSerializer, BaseGroupSerializer


class DeveloperPermissionSerializer(BasePermissionSerializer):
    class Meta:
        model = DeveloperPermission
        base_fields = BasePermissionSerializer.Meta.fields
        fields = base_fields


class DeveloperGroupSerializer(BaseGroupSerializer):
    class Meta:
        model = DeveloperGroup
        base_fields = BaseGroupSerializer.Meta.fields
        fields = base_fields
