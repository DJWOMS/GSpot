import rollbar
from dacite import MissingValueError, from_dict
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.base.schemas import PaymentServices

from .schemas import YookassaPaymentResponse
from .serializers import YookassaPaymentAcceptanceSerializer
from .services.payment_acceptance import proceed_payment_response


class YookassaPaymentAcceptanceView(CreateAPIView):
    serializer_class = YookassaPaymentAcceptanceSerializer

    def post(self, request, *args, **kwargs):
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
