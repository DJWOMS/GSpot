from base.serializers import BasePermissionSerializer
from developer.models import DeveloperPermission


class DeveloperPermissionSerializer(BasePermissionSerializer):
    class Meta:
        model = DeveloperPermission
        base_fields = BasePermissionSerializer.Meta.fields
        fields = base_fields
