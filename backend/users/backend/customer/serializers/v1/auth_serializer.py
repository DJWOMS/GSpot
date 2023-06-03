from base.serializers import BaseAuthSerializer
from customer.models import CustomerUser


class CustomerAuthSerializer(BaseAuthSerializer):
    class Meta:
        model = CustomerUser
        fields = ("email", "password")
