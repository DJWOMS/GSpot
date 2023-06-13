from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from administrator.models import BlockReason
from customer.models import CustomerUser


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'customer_list'
        model = CustomerUser
        fields = (
            'email',
            'avatar',
            'is_active',
            'is_banned',
        )


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'customer_retrieve'
        model = CustomerUser
        fields = (
            'birthday',
            'country',
            'phone',
            'created_at',
            'update_at',
            *CustomerListSerializer.Meta.fields,
        )


class CustomerBlockSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if len(attrs["reason"]) < 3:
            raise ValidationError(_("Reason message should be more than 3 symbols"))
        if not CustomerUser.objects.filter(pk=attrs.get('user')).exists():
            raise ValidationError(_("User doesn't exists"))
        return attrs

    def create(self, validated_data):
        user = CustomerUser.objects.get(pk=validated_data.get("pk"))
        user.is_banned = True
        user.save()
        return BlockReason.objects.create(**validated_data)

    class Meta:
        ref_name = 'customer_block'
        model = BlockReason
        fields = (
            'reason',
            'creator',
            'user',
        )


class CustomerRequestBlockSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'customer_req_block'
        model = BlockReason
        fields = ('reason',)
