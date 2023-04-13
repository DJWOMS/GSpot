import rollbar
from apps.external_payments.schemas import PaymentCreateDataClass, YookassaPaymentInfo
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from . import serializers
from .models import Account
import uuid

from .services.balance_change import request_balance_deposit_url
from .services.payment_commission import calculate_payment_with_commission


class CalculatePaymentCommissionView(CreateAPIView):
    serializer_class = serializers.PaymentCommissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            commission_data = YookassaPaymentInfo(**serializer.validated_data)
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}'
                'error',
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        amount_with_commission = calculate_payment_with_commission(
            commission_data.payment_type,
            commission_data.payment_amount,
        )
        return Response({'amount with commission': amount_with_commission})


class BalanceIncreaseView(CreateAPIView):
    serializer_class = serializers.BalanceIncreaseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            payment_data = PaymentCreateDataClass(
                **serializer.validated_data,
            )
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        confirmation_url = request_balance_deposit_url(payment_data)

        return Response(
            {'confirmation_url': confirmation_url},
            status=status.HTTP_201_CREATED,
        )


class AccountOwnerAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountOwnerSerializer
    lookup_field = 'user_uuid'

    def get_queryset(self):
        default_owner_uuid = uuid.UUID("333")
        return Account.objects.filter(user_uuid=default_owner_uuid)
