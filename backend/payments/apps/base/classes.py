from abc import ABC, abstractmethod
from typing import assert_never

import rollbar
from apps.base.exceptions import DifferentStructureError
from apps.item_purchases.exceptions import RefundNotAllowedError
from apps.item_purchases.models import ItemPurchase
from apps.item_purchases.schemas import ItemPurchaseData
from apps.item_purchases.services.item_purchase_completer import ItemPurchaseCompleter
from dacite import from_dict
from django.core.exceptions import MultipleObjectsReturned
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response


class AbstractPaymentService(ABC):
    @abstractmethod
    def request_balance_deposit_url(self, payment_data):
        pass

    @abstractmethod
    def handel_payment_response(self):
        pass

    @abstractmethod
    def parse_income_data(self, **kwargs):
        pass

    @abstractmethod
    def validate_income_data(self, parsed_data):
        pass


class AbstractPayoutService(ABC):
    @abstractmethod
    def request_payout(self, payout_data):
        pass


class DRFtoDataClassMixin:
    def convert_data(self, request, dataclass_model):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.__convert_drf_to_dataclass(dataclass_model, serializer)

    def __convert_drf_to_dataclass(self, data_model, serializer: dict):
        # TODO change to pydantic, add typehint for pydantic model  # noqa: T000
        try:
            data_model_data = from_dict(
                data_model,
                serializer.validated_data,
            )
        except AttributeError:
            data_model_data = data_model(**serializer.validated_data)
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            raise DifferentStructureError
        return data_model_data


class ItemPurchaseStatusChanger(DRFtoDataClassMixin):
    def update_item_purchase_status(
        self,
        request: Request,
        event_type: ItemPurchase.ItemPurchaseStatus,
    ) -> Response:
        try:
            item_purchase_data = self.convert_data(request, ItemPurchaseData)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = self.fetch_item_purchase(item_purchase_data)
        if type(response) != ItemPurchase:
            return response

        data = {'item_purchase': response}
        if event_type == ItemPurchase.ItemPurchaseStatus.PAID:
            # PAID because this function should be called only when it's gift
            data['is_gift'] = True

        try:
            item_purchase_processor = ItemPurchaseCompleter(**data)
        except RefundNotAllowedError as error:
            return Response(
                {'detail': str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        match event_type:
            case ItemPurchase.ItemPurchaseStatus.PAID:
                # PAID because this function should be called only when it's gift
                item_purchase_processor.accept_gift()
                return Response(status=status.HTTP_200_OK)
            case ItemPurchase.ItemPurchaseStatus.REFUNDED:
                item_purchase_processor.take_refund()
                return Response(status=status.HTTP_202_ACCEPTED)
            case _ as not_implemented:
                assert_never(not_implemented)

    def fetch_item_purchase(self, item_purchase_data: ItemPurchaseData) -> ItemPurchase | Response:
        try:
            item_purchase = ItemPurchase.objects.get(
                account_to__user_uuid=item_purchase_data.user_uuid,
                item_uuid=item_purchase_data.item_uuid,
                status=ItemPurchase.ItemPurchaseStatus.PENDING,
            )
        except ItemPurchase.DoesNotExist:
            return Response(
                {'detail': 'No such product for this user'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except MultipleObjectsReturned:
            rollbar.report_message(
                'Found several ItemPurchase instances while trying to update status '
                'for next query conditions: '
                f'account_to__user_uuid={item_purchase_data.user_uuid}, '
                f'item_uuid={item_purchase_data.item_uuid}, '
                f'status={ItemPurchase.ItemPurchaseStatus.PENDING} ',
                'error',
            )
            return Response(
                {'detail': 'internal server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return item_purchase
