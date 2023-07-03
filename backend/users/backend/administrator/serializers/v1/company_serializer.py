from administrator.models import CompanyModerate
from administrator.serializers.v1.developer_serializer import (
    DeveloperRetrieveSerializer,
)
from developer.models import Company
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "company_list"
        model = Company
        fields = (
            "email",
            "image",
            "is_active",
            "is_banned",
            "title",
        )


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    employers = DeveloperRetrieveSerializer(many=True, read_only=True)

    class Meta:
        ref_name = "company_retrieve"
        model = Company
        fields = (
            "created_by",
            "contact",
            "description",
            "is_confirmed",
            "created_at",
            *CompanyListSerializer.Meta.fields,
            "employers",
        )


class CompanyBlockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        company: Company = self.context["company"]
        if company.is_banned:
            raise ValidationError(_("Company is already banned"))
        return attrs

    def save(self, admin, company):
        CompanyModerate.objects.create(
            reason=self.validated_data["reason"],
            company=company,
            admin=admin,
            action="B",
        )
        company.is_banned = True
        company.save()

    class Meta:
        ref_name = "company_block"
        model = CompanyModerate
        fields = ("reason",)


class CompanyUnblockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        company: Company = self.context["company"]
        if not company.is_banned:
            raise ValidationError(_("Company is already active"))
        return attrs

    def save(self, admin, company):
        CompanyModerate.objects.create(
            reason=self.validated_data["reason"],
            company=company,
            admin=admin,
            action="U",
        )
        company.is_banned = False
        company.save()

    class Meta:
        ref_name = "company_unblock"
        model = CompanyModerate
        fields = ("reason",)
