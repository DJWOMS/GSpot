from rest_framework import serializers

from developer.models import CompanyUser


class DeveloperEmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'


class DeveloperEmployeeCreateSerializer(serializers.ModelSerializer):
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
