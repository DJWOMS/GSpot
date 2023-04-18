import rollbar
from apps.transactions.schemas import PurchaseItemsData
from dacite import MissingValueError, from_dict
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import PurchaseItemsSerializer
from .services.purchase_items import request_purchase_items


class PurchaseItemView(viewsets.GenericViewSet):
    serializer_class = PurchaseItemsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
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
        response = request_purchase_items(income_data)
        return Response({'response': response}, status=status.HTTP_200_OK)
