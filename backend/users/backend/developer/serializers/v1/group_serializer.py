from base.serializers import BaseGroupSerializer
from developer.models import DeveloperGroup, DeveloperPermission
from rest_framework import serializers


class DeveloperGroupSerializer(BaseGroupSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        queryset=DeveloperPermission.objects.all(),
        many=True,
    )

    class Meta:
        model = DeveloperGroup
        base_fields = BaseGroupSerializer.Meta.fields
        fields = base_fields
