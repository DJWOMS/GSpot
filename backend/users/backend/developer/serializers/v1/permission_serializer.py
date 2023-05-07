from developer.models import DeveloperPermission

from base.serializers import BasePermissionSerializer


class DeveloperPermissionSerializer(BasePermissionSerializer):
    class Meta:
        model = DeveloperPermission
        base_fields = BasePermissionSerializer.Meta.fields
        fields = base_fields
