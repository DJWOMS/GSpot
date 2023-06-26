from rest_framework import serializers
from developer.models import CompanyUser, Company
from rest_framework.exceptions import ValidationError


class CompanyCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        user = self.context["request"].user
        if Company.objects.filter(created_by=user).exists():
            raise ValidationError("User can create only one company")
        return attrs

    class Meta:
        model = Company
        fields = ("title", "description", "contact", "email", "created_by", "image")


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("title", "description", "contact", "email", "created_by", "image")
        read_only_fields = ("created_by",)
