from rest_framework import serializers

from administrator.models import AdminPermission, AdminGroup

from base.serializers import BasePermissionSerializer, BaseGroupSerializer


class AdminPermissionSerializer(BasePermissionSerializer):
    class Meta:
        model = AdminPermission
        base_fields = BasePermissionSerializer.Meta.fields
        fields = base_fields


class AdminGroupSerializer(BaseGroupSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        queryset=AdminPermission.objects.all(), many=True
    )

    class Meta:
        model = AdminGroup
        base_fields = BaseGroupSerializer.Meta.fields
        fields = base_fields
