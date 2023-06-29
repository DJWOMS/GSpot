from rest_framework import serializers

from customer.models import CustomerUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ("id", "username")


class AccountRetrieveSerializers(serializers.ModelSerializer):
    friends = UserSerializers(many=True)

    class Meta:
        ref_name = "customer_account_retrieve"
        model = CustomerUser
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
            "friends",
            "birthday",
        )


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = "customer_account_update"
        model = CustomerUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "avatar",
            "country",
            "birthday",
        )
