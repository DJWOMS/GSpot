from common.models import ContactType

from rest_framework import serializers


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = "__all__"
