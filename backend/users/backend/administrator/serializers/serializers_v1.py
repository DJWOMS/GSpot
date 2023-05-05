from administrator.models import AdminPermission, AdminGroup

from base.serializers import BasePermission, BaseGroup


class AdminPermissionSerializer(BasePermission):
    class Meta:
        model = AdminPermission
        base_fields = BasePermission.Meta.fields
        fields = base_fields


class AdminGroupSerializer(BaseGroup):
    class Meta:
        model = AdminGroup
        base_fields = BaseGroup.Meta.fields
        fields = base_fields
