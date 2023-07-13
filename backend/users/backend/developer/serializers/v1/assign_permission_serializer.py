from rest_framework import serializers
from developer.models import CompanyUser, DeveloperPermission, DeveloperGroup

class DeveloperPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperPermission
        fields = ['id']

class DeveloperGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperGroup
        fields = ['id']

class CompanyUserPermissionSerializer(serializers.ModelSerializer):
    user_permissions = DeveloperPermissionSerializer(many=True)
    groups = DeveloperGroupSerializer(many=True)

    class Meta:
        model = CompanyUser
        fields = ['id', 'user_permissions', 'groups']

    def create(self, validated_data):
        permissions_data = validated_data.pop('user_permissions')
        groups_data = validated_data.pop('groups')
        instance = CompanyUser.objects.create(**validated_data)
        instance.user_permissions.set(permissions_data)
        instance.groups.set(groups_data)
        return instance
