import json
from decimal import Decimal

import rollbar
from django.core.exceptions import ObjectDoesNotExist
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
            serialized_data = serializer.validated_data
        else:
            return Response(400)

        confirmation_url = create_payment(
            uuid=serialized_data.get('uuid'),
            value=serialized_data.get('value'),
            commission=serialized_data.get('commission'),
            payment_type=serialized_data.get('payment_type'),
            return_url=serialized_data.get('return_url'),
        )

        return Response({'confirmation_url': confirmation_url}, 200)


class CreatePaymentAcceptanceView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        response = json.loads(request.body)

        try:
            table = BalanceChange.objects.get(
                id=response['object']['metadata']['table_id'],
            )
        except ObjectDoesNotExist:
            rollbar.report_message(
                "Can't get table for payment id {0}".format(
                    response['object']['id'],
                ),
                'warning',
            )
            return Response(404)

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
