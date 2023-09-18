from administrator.models import CustomerModerate
from customer.models import CustomerUser
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "customer_list"
        model = CustomerUser
        fields = ("email", "avatar", "is_active", "is_banned", "username")


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "customer_retrieve"
        model = CustomerUser
        fields = (
            "birthday",
            "country",
            "phone",
            "created_at",
            "update_at",
            *CustomerListSerializer.Meta.fields,
        )


class CustomerBlockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        customer: CustomerUser = self.context["customer"]
        if customer.is_banned:
            raise ValidationError(_("User is already banned"))

        return attrs

    def save(self, admin, customer):
        CustomerModerate.objects.create(
            reason=self.validated_data["reason"],
            customer=customer,
            admin=admin,
            action="B",
        )
        customer.is_banned = True
        customer.save()

    class Meta:
        ref_name = "customer_block"
        model = CustomerModerate
        fields = ("reason",)


class CustomerUnblockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        customer: CustomerUser = self.context["customer"]
        if not customer.is_banned:
            raise ValidationError(_("User is already active"))

        return attrs

    def save(self, admin, customer):
        CustomerModerate.objects.create(
            reason=self.validated_data["reason"],
            customer=customer,
            admin=admin,
            action="U",
        )
        customer.is_banned = False
        customer.save()

    class Meta:
        ref_name = "customer_unblock"
        model = CustomerModerate
        fields = ("reason",)
