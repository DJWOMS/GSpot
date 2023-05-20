from rest_framework import serializers

from developer.models import CompanyUser


class DeveloperRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """send totp"""
        return CompanyUser.objects.create_user(**validated_data, is_superuser=False)

    class Meta:
        model = CompanyUser
        exclude = (
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions',
            'is_banned',
        )
