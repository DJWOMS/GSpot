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
        banned_user: CustomerUser = self.context['user']
        if banned_user.is_banned:
            raise ValidationError(_('User already banned'))
        return attrs

    def save(self, creator):
        return BlockReason.objects.create(
            reason=self.validated_data['reason'], creator=creator, user=self.context['user']
        )

    class Meta:
        ref_name = 'customer_block'
        model = BlockReason
        fields = ('reason',)
