from common.mixins import TOTPVerificationMixin
from customer.serializers.v1.customer_registration_serializer import (
    CustomerRegistrationSerializer,
)
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny


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
