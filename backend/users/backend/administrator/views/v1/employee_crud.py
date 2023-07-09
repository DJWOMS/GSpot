from administrator.models import Admin
from administrator.serializers.v1.employee_crud import (
    EmployeeCreateUpdateSerializer,
    EmployeeListSerializer,
    EmployeeRetrieveSerializer,
    EmployeeSendEmailSerializer,
)
from base.views import PartialUpdateMixin
from common.mixins import TOTPVerificationMixin
from common.permissions.permissons import IsAdminSuperUserPerm
from common.services.totp import TOTPToken
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_description="Список сотрудников администраторов",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            200: openapi.Response("Список администраторов", EmployeeListSerializer(many=True)),
            403: openapi.Response("Отсутствуют права на просмотр списка сотрудников"),
        },
    ),
)
@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_description="Добавить сотрудника администратора",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            201: openapi.Response("Административный сотрудник", EmployeeCreateUpdateSerializer),
            400: openapi.Response("Данные не валидны"),
            403: openapi.Response("Отсутствуют права на создание администратора"),
        },
    ),
)
class EmployeeListView(TOTPVerificationMixin, generics.ListCreateAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    http_method_names = ["get", "post"]
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeListSerializer
        elif self.request.method == "POST":
            return EmployeeCreateUpdateSerializer


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_description="Подробные данные об администраторе",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            200: openapi.Response(
                "Личная информация администратора",
                EmployeeRetrieveSerializer,
            ),
            403: openapi.Response(
                "Отсутствуют права на просмотр подробной информации об администраторе",
            ),
            404: openapi.Response("Администратор не найден"),
        },
    ),
)
@method_decorator(
    name="put",
    decorator=swagger_auto_schema(
        operation_description="Изменить данные об администраторе",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            200: openapi.Response(
                "Личная информация администратора",
                EmployeeCreateUpdateSerializer,
            ),
            400: openapi.Response("Данные не валидны"),
            403: openapi.Response("Отсутствуют права на изменение данных об администраторе"),
            404: openapi.Response("Администратор не найден"),
        },
    ),
)
@method_decorator(
    name="delete",
    decorator=swagger_auto_schema(
        operation_description="Удалить администратора",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            204: openapi.Response(
                "Администратор удален",
            ),
            403: openapi.Response("Отсутствуют права на удаление администратора"),
            404: openapi.Response("Администратор не найден"),
        },
    ),
)
class EmployeeDetailView(PartialUpdateMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    http_method_names = ["get", "put", "delete"]
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeRetrieveSerializer
        elif self.request.method == "PUT":
            return EmployeeCreateUpdateSerializer


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_description="Отправить на email повторный запрос для авторизации",
        tags=["Администратор", "Административная панель владельца"],
        responses={
            200: openapi.Response(
                "Email администратора на который отправлен totp для регистрации",
                EmployeeSendEmailSerializer,
            ),
            404: openapi.Response("Администратор не найден"),
            403: openapi.Response(
                "Отсутствуют права на повторную отправку email для регистрации администратора",
            ),
        },
    ),
)
class EmployeeSendEmail(TOTPVerificationMixin, APIView):
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    serializer_class = EmployeeSendEmailSerializer

    def post(self, request, pk):
        admin = Admin.objects.get(pk=pk, is_active=False)
        serializer = self.serializer_class(instance=admin, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        TOTPToken().send_totp(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
