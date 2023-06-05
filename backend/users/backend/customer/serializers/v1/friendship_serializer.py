from rest_framework import serializers

from customer.models import FriendShipRequest


class FriendShipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendShipRequest
        fields = ['id', 'status', 'sender', 'receiver']
        read_only_fields = ['id', 'status', 'sender', 'receiver']
