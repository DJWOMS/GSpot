from administrator.models import Admin
from administrator.serializers import account_serializers
from base.views import PersonalAccount
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Личный кабинет пользователя",
        tags=["Администратор", "Личный кабинет администратора"],
        responses={
            200: openapi.Response(
                "Личная информация администратора",
                account_serializers.AccountRetrieveSerializers,
            ),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Изменение информации в личном кабинете пользователя",
        tags=["Администратор", "Личный кабинет администратора"],
        responses={
            200: openapi.Response(
                "Личная информация администратора",
                account_serializers.AccountUpdateSerializers,
            ),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление профиля администратора",
        tags=["Администратор", "Личный кабинет администратора"],
        responses={
            204: openapi.Response("Профиль администратора успешно удалён"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
class AccountViewSet(PersonalAccount):
    queryset = Admin.objects.all()
    http_method_names = ["get", "put", "delete"]

    serializer_map = {
        "default": account_serializers.AccountRetrieveSerializers,
        "retrieve": account_serializers.AccountRetrieveSerializers,
        "partial_update": account_serializers.AccountUpdateSerializers,
        "destroy": account_serializers.AccountRetrieveSerializers,
    }

    permission_map = {
        "default": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }
