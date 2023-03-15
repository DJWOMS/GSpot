import json
from decimal import Decimal

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Account, BalanceChange
from .serializers import CreatePaymentSerializer
from .services.create_payment import create_payment


class CreatePaymentView(CreateAPIView):
    serializer_class = CreatePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreatePaymentSerializer(data=request.POST)

        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(400)

        confirmation_url = create_payment(
            uuid=data.get('uuid'),
            value=data.get('value'),
            commission=data.get('commission'),
            payment_type=data.get('payment_type'),
            return_url=data.get('return_url'),
        )

        return Response({'confirmation_url': confirmation_url}, 200)


class CreatePaymentAcceptanceView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        response = json.loads(request.body)
        table = BalanceChange.objects.get(
            id=response['object']['metadata']['table_id'],
        )

        if response['event'] == 'payment.succeeded':
            table.is_accepted = True
            table.save()
            Account.deposit(
                pk=response['object']['metadata']['user_id'],
                amount=Decimal(response['object']['income_amount']['value']),
            )
        elif response['event'] == 'payment.canceled':
            table.delete()

        return Response(200)
