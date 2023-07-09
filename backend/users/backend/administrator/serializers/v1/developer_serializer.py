from administrator.models import CompanyUserModerate
from developer.models import CompanyUser
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class DeveloperListSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "developer_list"
        model = CompanyUser
        fields = (
            "email",
            "avatar",
            "is_active",
            "is_banned",
            "username",
            "company",
        )


class DeveloperRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "developer_retrieve"
        model = CompanyUser
        fields = (
            "country",
            "phone",
            "created_at",
            "update_at",
            *DeveloperListSerializer.Meta.fields,
        )


class DeveloperBlockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        company_user: CompanyUser = self.context["company_user"]
        if company_user.is_banned:
            raise ValidationError(_("User is already banned"))
        return attrs

    def save(self, admin, company_user: CompanyUser):
        CompanyUserModerate.objects.create(
            reason=self.validated_data["reason"],
            company_user=company_user,
            admin=admin,
            action="B",
        )
        company_user.is_banned = True
        company_user.save()

    class Meta:
        ref_name = "developer_block"
        model = CompanyUserModerate
        fields = ("reason",)


class DeveloperUnblockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        company_user: CompanyUser = self.context["company_user"]
        if not company_user.is_banned:
            raise ValidationError(_("User is already active"))
        return attrs

    def save(self, admin, company_user: CompanyUser):
        CompanyUserModerate.objects.create(
            reason=self.validated_data["reason"],
            company_user=company_user,
            admin=admin,
            action="U",
        )
        company_user.is_banned = False
        company_user.save()

    class Meta:
        ref_name = "developer_unblock"
        model = CompanyUserModerate
        fields = ("reason",)
