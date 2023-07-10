from apps.base.classes import DRFtoDataClassMixin
from apps.base.exceptions import AttemptsLimitExceededError, DifferentStructureError
from apps.base.utils.db_query import multiple_select_or_404
from apps.external_payments.schemas import YookassaPayoutModel
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from ..external_payments.models import BalanceServiceMap
from . import serializers
from .exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError,
)
from .models import Account, BalanceChange, Owner, PayoutData
from .schemas import BalanceIncreaseData, CommissionCalculationInfo
from .serializers import CreatePayoutDataSerializer
from .services.balance_change import request_balance_deposit_url
from .services.payment_commission import PaymentCalculation
from .services.payout import PayoutProcessor


class CalculatePaymentCommissionView(viewsets.ViewSet, DRFtoDataClassMixin):
    serializer_class = serializers.PaymentCommissionSerializer

    def create(self, request, *args, **kwargs):
        try:
            commission_data = self.convert_data(request, CommissionCalculationInfo)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        amount_with_commission = PaymentCalculation(
            payment_type=commission_data.payment_type,
            payment_service=commission_data.payment_service,
            payment_amount=commission_data.payment_amount,
        ).calculate_payment_with_commission()

        return Response({'amount with commission': amount_with_commission})


class BalanceIncreaseView(viewsets.ViewSet, DRFtoDataClassMixin):
    serializer_class = serializers.BalanceIncreaseSerializer

    def create(self, request, *args, **kwargs):
        try:
            balance_increase_data = self.convert_data(request, BalanceIncreaseData)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        confirmation_url = request_balance_deposit_url(balance_increase_data)
        return Response(
            {'confirmation_url': confirmation_url},
            status=status.HTTP_201_CREATED,
        )


class UserCreateDeleteView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = serializers.AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'user_uuid'

    def create(self, request, *args, **kwargs):
        uuid = request.data.get('user_uuid')
        if Account.objects.filter(user_uuid=uuid).exists():
            return Response(
                {'error': 'A user with this UUID already exists'},
                status=status.HTTP_409_CONFLICT,
            )
        return super().create(request, *args, **kwargs)


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


class OwnerView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = serializers.OwnerSerializer

    def get_object(self):
        return Owner.objects.first()


class PayoutDataObjectViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.PayoutDataSerializer
    queryset = PayoutData.objects.all()

    def partial_update(self, request, *args, **kwargs):
        payout_data_obj = self.get_object()
        data = request.data

        for field_name in ('account_number', 'is_auto_payout', 'payout_type'):
            field_data = data.get(field_name, getattr(payout_data_obj, field_name))
            setattr(payout_data_obj, field_name, field_data)

        serializer_data = model_to_dict(payout_data_obj)
        payout_serializers = self.get_serializer(data=serializer_data)
        payout_serializers.is_valid(raise_exception=True)
        payout_data_obj.save()
        return Response(payout_serializers.validated_data)


class PayoutDataCreateView(viewsets.ViewSet):
    serializer_class = CreatePayoutDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        developer_account = get_object_or_404(
            Account,
            user_uuid=serializer.validated_data['user_uuid'],
        )
        if PayoutData.objects.filter(user_uuid=developer_account).exists():
            return Response(
                f'Payout data for this {developer_account} already exists',
                status.HTTP_400_BAD_REQUEST,
            )

        validated_data = serializer.validated_data.copy()
        validated_data['user_uuid'] = developer_account
        serializer.create(validated_data=validated_data)
        return Response(serializer.validated_data, status.HTTP_201_CREATED)


class PayoutHistoryView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.BalanceHistorySerializer

    def get_queryset(self):
        user_uuid = self.kwargs.get('user_uuid')
        account = get_object_or_404(Account, user_uuid=user_uuid)
        queryset = BalanceChange.objects.filter(
            account_id=account,
            operation_type=BalanceChange.OperationType.WITHDRAW,
            balanceservicemap__operation_type=BalanceServiceMap.OperationType.PAYOUT,
        )
        return queryset


class RefillHistoryView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.BalanceHistorySerializer

    def get_queryset(self):
        user_uuid = self.kwargs.get('user_uuid')
        account = get_object_or_404(Account, user_uuid=user_uuid)
        queryset = BalanceChange.objects.filter(
            account_id=account,
            operation_type=BalanceChange.OperationType.DEPOSIT,
            balanceservicemap__operation_type=BalanceServiceMap.OperationType.PAYMENT,
        )
        return queryset
