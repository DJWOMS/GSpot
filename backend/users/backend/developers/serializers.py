from rest_framework import serializers
from .models import CompanyUser, Company


class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('email', 'description', 'poster', 'created_by')


class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'
