from developer.models import DeveloperPermission, DeveloperGroup

from base.serializers import BasePermission, BaseGroup


class DeveloperPermissionSerializer(BasePermission):
    class Meta:
        model = DeveloperPermission
        base_fields = BasePermission.Meta.fields
        fields = base_fields


class DeveloperGroupSerializer(BaseGroup):
    class Meta:
        model = DeveloperGroup
        base_fields = BaseGroup.Meta.fields
        fields = base_fields
