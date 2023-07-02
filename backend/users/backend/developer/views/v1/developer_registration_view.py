from common.mixins import TOTPVerificationMixin
from developer.serializers.v1.developer_registration_serializer import (
    DeveloperRegistrationSerializer,
)
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_description="Зарегистрировать разработчика",
        tags=[
            "Разработчик",
            "Административная панель разработчика",
        ],
        request_body=DeveloperRegistrationSerializer,
        responses={
            201: openapi.Response("Пользователь зарегистрирован"),
            400: openapi.Response("Данные не валидны"),
        },
    ),
)
class DeveloperRegistrationView(TOTPVerificationMixin, generics.CreateAPIView):
    serializer_class = DeveloperRegistrationSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
