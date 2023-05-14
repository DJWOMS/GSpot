import rollbar
from apps.base.exceptions import AttemptsLimitExceededError
from apps.item_purchases.schemas import PurchaseItemsData
from apps.payment_accounts.exceptions import InsufficientFundsError
from dacite import MissingValueError, from_dict
from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import PurchaseItemsSerializer
from .services.purchase_items import ItemPurchaseRequest


class PurchaseItemView(viewsets.ViewSet):
    serializer_class = PurchaseItemsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            income_data = from_dict(
                PurchaseItemsData,
                serializer.validated_data,
            )
        except MissingValueError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
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
