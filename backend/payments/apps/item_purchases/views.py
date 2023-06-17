from apps.base.classes import DRFtoDataClassMixin, ItemPurchaseStatusChanger
from apps.base.exceptions import AttemptsLimitExceededError, DifferentStructureError
from apps.payment_accounts.exceptions import InsufficientFundsError
from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ItemPurchase
from .schemas import PurchaseItemsData
from .serializers import PurchaseItemsSerializer, RefundSerializer
from .services.item_purchase_creator import ItemPurchaseRequest


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


class ItemPurchaseUpdaterViewSet(viewsets.ViewSet, ItemPurchaseStatusChanger):
    serializer_class = RefundSerializer

    @action(detail=False, methods=['post'])
    def request_refund(self, request, *args, **kwargs):
        return self.update_item_purchase_status(request, ItemPurchase.ItemPurchaseStatus.REFUNDED)

    @action(detail=False, methods=['post'])
    def accept_gift(self, request, *args, **kwargs):
        return self.update_item_purchase_status(request, ItemPurchase.ItemPurchaseStatus.PAID)
