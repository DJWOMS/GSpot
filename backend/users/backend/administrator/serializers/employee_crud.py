from rest_framework import serializers

from administrator.models import Admin


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Admin.objects.create(**validated_data, is_superuser=False, is_active=False)

    class Meta:
        model = Admin
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'country',
        )


class EmployeeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
