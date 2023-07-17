from common.mixins import TOTPVerificationMixin
from customer.models import CustomerUser
from customer.serializers.v1.customer_registration_serializer import (
    CustomerRegistrationSerializer,
)
from customer.tasks import create_payment_account
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_description="Зарегистрировать пользователя",
        tags=[
            "Пользователь",
        ],
        request_body=CustomerRegistrationSerializer,
        responses={
            201: openapi.Response("Пользователь зарегистрирован"),
            400: openapi.Response("Данные не валидны"),
        },
    ),
)
class CustomerRegistrationView(TOTPVerificationMixin, generics.CreateAPIView):
    http_method_names = ["post"]
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CustomerRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # get users_id and push to celery task
        user_uuid = serializer.instance.id
        create_payment_account(user_uuid)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
