from administrator.serializers import account_serializers as admin_account_serializers
from customer.serializers import account_serializers as customer_account_serializers
from developer.serializers import account_serializers as developer_account_serializers
from rest_framework import serializers


class MixedAccountRetrieveSerializer(serializers.Serializer):
    administrators = admin_account_serializers.AccountRetrieveSerializers(many=True, read_only=True)
    developers = developer_account_serializers.AccountRetrieveSerializers(many=True, read_only=True)
    customers = customer_account_serializers.AccountRetrieveSerializers(many=True, read_only=True)

    def to_representation(self, instance):
        administrators = instance.filter(role='administrator')
        developers = instance.filter(role='developer')
        customers = instance.filter(role='customer')
        return {
            'administrators': admin_account_serializers.AccountRetrieveSerializers(
                administrators,
                many=True,
            ).data,
            'developers': developer_account_serializers.AccountRetrieveSerializers(
                developers,
                many=True,
            ).data,
            'customers': customer_account_serializers.AccountRetrieveSerializers(
                customers,
                many=True,
            ).data,
        }
