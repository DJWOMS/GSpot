from rest_framework import serializers

from administrator.models import BlockReason
from customer.models import CustomerUser


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'customer_list'
        model = CustomerUser
        fields = (
            'birthday',
            'avatar',
            'country',
            'email',
            'phone',
            'created_at',
            'update_at',
            'is_active',
            'is_banned',
        )


class CustomerBlockSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = CustomerUser.objects.get(pk=validated_data.get("pk"))
        user.is_banned = True
        user.save()
        return BlockReason.objects.create(**validated_data)

    class Meta:
        ref_name = 'customer_block'
        model = BlockReason
        fields = (
            'reason',
            'creator',
            'user',
        )
