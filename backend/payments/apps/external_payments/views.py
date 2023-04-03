import rollbar
from dacite import from_dict, MissingValueError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .schemas import YookassaPaymentResponse
from .serializers import YookassaPaymentAcceptanceSerializer
from .services.accept_payment import yookassa_payment_acceptance


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
            return

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
            return

        if yookassa_payment_acceptance(yookassa_data):
            return Response(200)
        return Response(404)
