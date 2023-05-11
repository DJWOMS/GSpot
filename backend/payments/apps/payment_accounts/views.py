import rollbar
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from . import serializers
from .models import Account
from .schemas import BalanceIncreaseData, CommissionCalculationInfo
from .services.balance_change import request_balance_deposit_url
from .services.payment_commission import calculate_payment_with_commission


class CalculatePaymentCommissionView(CreateAPIView):
    serializer_class = serializers.PaymentCommissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            commission_data = CommissionCalculationInfo(**serializer.validated_data)
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
            balance_increase_data = BalanceIncreaseData(
                **serializer.validated_data,
            )
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        confirmation_url = request_balance_deposit_url(balance_increase_data)

        return Response(
            {'confirmation_url': confirmation_url},
            status=status.HTTP_201_CREATED,
        )


class UserAccountAPIView(CreateAPIView):
    serializer_class = serializers.AccountSerializer


class AccountBalanceViewSet(viewsets.ViewSet):
    def retrieve(self, request, user_uuid=None):
        account = get_object_or_404(Account, user_uuid=user_uuid)
        serializer = serializers.AccountBalanceSerializer(account)
        return Response(serializer.data)


class BalanceViewSet(viewsets.ViewSet):
    serializer_class = serializers.UUIDSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        uuid_list = serializer.validated_data['uuid_list']
        user_balance_datas = []

        for uuid in uuid_list:
            obj = get_object_or_404(Account, user_uuid=uuid)
            balance = {'balance': obj.balance}

            money_serializer = serializers.MoneySerializer(data=balance)
            money_serializer.is_valid(raise_exception=True)

            balance_dict = {'user_uuid': str(uuid)}
            balance_dict.update(money_serializer.validated_data)
            user_balance_datas.append(balance_dict)

        return Response(user_balance_datas)
