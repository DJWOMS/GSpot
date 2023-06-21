from rest_framework import serializers
from developer.models import CompanyUser, Company


class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("title", "description", "contact", "email", "created_by", "image")


class CompanyEmployeeSerializer(CompanySerializer):
    class Meta:
        model = Company
        fields = ("email", "description", "image", "created_by")
