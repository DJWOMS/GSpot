import rollbar
from dacite import MissingValueError, from_dict
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .schemas import YookassaPaymentResponse
from .serializers import YookassaPaymentAcceptanceSerializer
from .services.accept_payment import PaymentAcceptance


class PaymentAcceptanceView(CreateAPIView):
    serializer_class = YookassaPaymentAcceptanceSerializer

    def post(self, request, *args, **kwargs):
        # I think we should store that request.data somewhere,
        # until this function is not finished
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            rollbar.report_message(
                "Can't parse response from yookassa.",
                'error',
            )
            return Response(200)

        try:
            # used from_dict function because
            # dataclasses cant parse nested models properly
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

        if PaymentAcceptance(yookassa_data).payment_status is True:
            return Response(200)
        return Response(404)
