from rest_framework import serializers

from developer.models import CompanyUser


class DeveloperEmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'country',
        )


class DeveloperEmployeeCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """send totp"""
        return CompanyUser.objects.create(**validated_data)

    class Meta:
        model = CompanyUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'country',
            'avatar',
            'is_banned',
        )


class DeveloperEmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'
