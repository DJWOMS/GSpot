from rest_framework import serializers

from administrator.models import Admin


class AccountRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "admin_account_retrieve"
        model = Admin
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
        )


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "admin_account_update"
        model = Admin
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "avatar",
            "country",
        )
