from rest_framework import serializers

from developer.models import DeveloperPermission, DeveloperGroup
from base.serializers import BaseGroupSerializer


class DeveloperGroupSerializer(BaseGroupSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        queryset=DeveloperPermission.objects.all(), many=True
    )

    class Meta:
        model = DeveloperGroup
        base_fields = BaseGroupSerializer.Meta.fields
        fields = base_fields
