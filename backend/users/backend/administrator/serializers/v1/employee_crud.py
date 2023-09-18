from administrator.models import Admin
from rest_framework import serializers


class EmployeeListSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Admin
        exclude = (
            "password",
            "groups",
            "user_permissions",
            "developer_groups",
            "developer_permissions",
        )


class EmployeeCreateUpdateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """send totp"""
        return Admin.objects.create(**validated_data, is_superuser=False, is_active=False)

    class Meta:
        model = Admin
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "country",
            "avatar",
            "is_banned",
        )


class EmployeeRetrieveSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Admin
        exclude = ("password",)


class EmployeeSendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
