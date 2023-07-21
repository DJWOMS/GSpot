from developer.models import CompanyUser
from rest_framework import serializers


class DeveloperRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """send totp"""
        return CompanyUser.objects.create_superuser(
            **validated_data,
            is_superuser=True,
            is_active=False,
        )

    class Meta:
        model = CompanyUser
        exclude = (
            "is_active",
            "is_superuser",
            "groups",
            "user_permissions",
            "is_banned",
            "password",
        )
