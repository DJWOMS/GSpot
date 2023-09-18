from developer.models import CompanyUser
from rest_framework import serializers


class AccountRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "developer_account_retrieve"
        model = CompanyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "created_at",
            "update_at",
            "avatar",
            "country",
            "company",
        )


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "developer_account_update"
        model = CompanyUser
        fields = ("username", "first_name", "last_name", "email", "phone", "avatar", "country")
