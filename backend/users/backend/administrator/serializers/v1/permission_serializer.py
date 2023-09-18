from administrator.models import AdminPermission
from base.serializers import BasePermissionSerializer


class AdminPermissionSerializer(BasePermissionSerializer):
    class Meta:
        model = AdminPermission
        base_fields = BasePermissionSerializer.Meta.fields
        fields = base_fields
