from administrator.models import AdminGroup, AdminPermission
from base.serializers import BaseGroupSerializer
from rest_framework import serializers


class AdminGroupSerializer(BaseGroupSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        queryset=AdminPermission.objects.all(),
        many=True,
    )

    class Meta:
        model = AdminGroup
        base_fields = BaseGroupSerializer.Meta.fields
        fields = base_fields
