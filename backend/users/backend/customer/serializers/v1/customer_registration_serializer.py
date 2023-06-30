from rest_framework import serializers

from customer.models import CustomerUser


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """send totp"""
        return CustomerUser.objects.create_user(**validated_data, is_active=False)

    class Meta:
        model = CustomerUser
        exclude = ('is_active', 'friends', 'is_banned', 'password')
