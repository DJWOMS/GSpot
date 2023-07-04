from apps.base.classes import DRFtoDataClassMixin
from apps.base.exceptions import AttemptsLimitExceededError, DifferentStructureError
from apps.payment_accounts.exceptions import InsufficientFundsError
from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from .models import ItemPurchase
from .schemas import PurchaseItemsData
from .serializers import (
    ItemPurchaseHistorySerializer,
    PurchaseItemsSerializer,
    RefundSerializer,
)
from .services.item_purchase_completer import ItemPurchaseStatusChanger
from .services.item_purchase_creator import ItemPurchaseHistoryData, ItemPurchaseRequest


class PurchaseItemView(viewsets.ViewSet, DRFtoDataClassMixin):
    serializer_class = PurchaseItemsSerializer

    def create(self, request, *args, **kwargs):
        try:
            income_data = self.convert_data(request, PurchaseItemsData)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            item_purchase_request = ItemPurchaseRequest(income_data)
        except (InsufficientFundsError, ValidationError, AttemptsLimitExceededError) as error:
            return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as error:
            return Response(
                {'detail': str(error)},
                status=status.HTTP_404_NOT_FOUND,
            )

        response = item_purchase_request.request_items_purchase()
        return Response({'response': response}, status=status.HTTP_200_OK)


class ItemPurchaseUpdateView(viewsets.ViewSet, ItemPurchaseStatusChanger):
    serializer_class = RefundSerializer

    @action(detail=False, methods=['post'])
    def request_refund(self, request, *args, **kwargs):
        return self.update_item_purchase_status(request, ItemPurchase.ItemPurchaseStatus.REFUNDED)

    @action(detail=False, methods=['post'])
    def accept_gift(self, request, *args, **kwargs):
        return self.update_item_purchase_status(request, ItemPurchase.ItemPurchaseStatus.PAID)


class ItemPurchaseHistoryView(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ItemPurchaseHistorySerializer

    def get_queryset(self):
        return ItemPurchaseHistoryData(self.kwargs['user_uuid']).get_item_purchase_qs()
