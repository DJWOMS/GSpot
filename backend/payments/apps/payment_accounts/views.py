from apps.base.classes import DRFtoDataClassMixin
from apps.base.exceptions import AttemptsLimitExceededError, DifferentStructureError
from apps.base.utils.db_query import multiple_select_or_404
from apps.external_payments.schemas import YookassaPayoutModel
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from . import serializers
from .exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError,
)
from .models import Account
from .schemas import BalanceIncreaseData, CommissionCalculationInfo
from .services.balance_change import request_balance_deposit_url
from .services.payment_commission import calculate_payment_with_commission
from .services.payout import PayoutProcessor


class CalculatePaymentCommissionView(CreateAPIView, DRFtoDataClassMixin):
    serializer_class = serializers.PaymentCommissionSerializer

    def post(self, request, *args, **kwargs):
        try:
            commission_data = self.convert_data(request, CommissionCalculationInfo)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        amount_with_commission = calculate_payment_with_commission(
            commission_data.payment_type,
            commission_data.payment_amount,
        )
        return Response({'amount with commission': amount_with_commission})


class BalanceIncreaseView(CreateAPIView, DRFtoDataClassMixin):
    serializer_class = serializers.BalanceIncreaseSerializer

    def post(self, request, *args, **kwargs):
        try:
            balance_increase_data = self.convert_data(request, BalanceIncreaseData)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        confirmation_url = request_balance_deposit_url(balance_increase_data)
        return Response(
            {'confirmation_url': confirmation_url},
            status=status.HTTP_201_CREATED,
        )


class UserAccountAPIView(CreateAPIView, DRFtoDataClassMixin):
    serializer_class = serializers.AccountSerializer


class PayoutView(viewsets.ViewSet, DRFtoDataClassMixin):
    serializer_class = serializers.PayoutSerializer

    def create(self, request, *args, **kwargs):
        try:
            payout_data = self.convert_data(request, YookassaPayoutModel)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        pre_payout_processor = PayoutProcessor(payout_data)
        try:
            response = pre_payout_processor.create_payout()
        except (
            NotPayoutDayError,
            InsufficientFundsError,
            AttemptsLimitExceededError,
            NotImplementedError,
            NotValidAccountNumberError,
        ) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'payout status': response})


class BalanceViewSet(viewsets.ViewSet):
    serializer_class = serializers.UUIDSerializer
    balance_serializer_class = serializers.BalanceSerializer

    def list(self, request, *args, **kwargs):  # noqa: A003
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        uuid_list = serializer.validated_data['uuid_list']
        try:
            balance_list = multiple_select_or_404(uuid_list, Account, 'user_uuid')
        except Http404 as error:
            return Response({'detail': str(error)}, status=status.HTTP_404_NOT_FOUND)

        return Response([self.balance_serializer_class(obj).data for obj in balance_list])

    def retrieve(self, request, user_uuid=None):
        account = get_object_or_404(Account, user_uuid=user_uuid)
        return Response(self.balance_serializer_class(account).data)
