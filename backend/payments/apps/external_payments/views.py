import rollbar
from apps.base.schemas import PaymentServices
from dacite import MissingValueError, from_dict
from rest_framework import viewsets
from rest_framework.response import Response

from .models import PaymentCommission, PaymentService
from .schemas import YookassaPaymentResponse
from .serializers import (
    PaymentCommissionSerializer,
    PaymentServiceSerializer,
    YookassaPaymentAcceptanceSerializer,
)
from .services.check_yookassa_response import check_yookassa_response
from .services.payment_acceptance import proceed_payment_response


class YookassaPaymentAcceptanceView(viewsets.GenericViewSet):
    serializer_class = YookassaPaymentAcceptanceSerializer

    def create(self, request, *args, **kwargs):
        yookassa_object = request.data.get('object')
        if yookassa_object is None or not check_yookassa_response(yookassa_object):
            rollbar.report_message(
                'Response not from yookassa.',
                'warning',
            )
            return Response(404)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            rollbar.report_message(
                "Can't parse response from yookassa.",
                'error',
            )
            return Response(200)

        try:
            yookassa_data = from_dict(
                YookassaPaymentResponse,
                serializer.validated_data,
            )
        except MissingValueError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            return Response(200)
        payment_status = proceed_payment_response(
            yookassa_data,
            PaymentServices.yookassa,
        )
        if payment_status is True:
            return Response(200)
        return Response(404)


class PaymentCommissionView(viewsets.ModelViewSet):
    serializer_class = PaymentCommissionSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.method == 'LIST':
            service_name = self.request.query_params.get('service_name')
            service = PaymentService.objects.get(name=service_name)
            return PaymentCommission.objects.filter(payment_service_id=service)
        return PaymentCommission.objects.all()


class PaymentServiceView(viewsets.ModelViewSet):
    queryset = PaymentService.objects.all()
    serializer_class = PaymentServiceSerializer
    pagination_class = None
