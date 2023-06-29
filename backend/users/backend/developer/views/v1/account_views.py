from django.utils.decorators import method_decorator

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated

from base.views import PersonalAccount
from developer.models import CompanyUser
from developer.serializers.account_serializers import (
    AccountRetrieveSerializers,
    AccountUpdateSerializers,
)


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Личный кабинет пользователя",
        tags=["Разработчик", "Личный кабинет разработчика"],
        responses={
            200: openapi.Response(
                "Личная информация пользователя",
                AccountRetrieveSerializers,
            ),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Изменение информации в личном кабинете пользователя",
        tags=["Разработчик", "Личный кабинет разработчика"],
        responses={
            200: openapi.Response("Информация обновлена", AccountUpdateSerializers),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление своего профиля самим пользователем",
        tags=["Разработчик", "Личный кабинет разработчика"],
        responses={
            200: openapi.Response("профиль успешно удалён"),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
class AccountViewSet(PersonalAccount):
    queryset = CompanyUser.objects.all()
    http_method_names = ["get", "put", "delete"]

    serializer_map = {
        "default": AccountRetrieveSerializers,
        "retrieve": AccountRetrieveSerializers,
        "partial_update": AccountUpdateSerializers,
        "destroy": AccountRetrieveSerializers,
    }

    permission_map = {
        "default": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }
