from base.views import PersonalAccount
from customer.models import CustomerUser
from customer.serializers import account_serializers
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Личный кабинет пользователя",
        tags=["Пользователь", "Личный кабинет пользователя"],
        responses={
            200: openapi.Response(
                "Личная информация пользователя",
                account_serializers.AccountRetrieveSerializers,
            ),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_description="Изменение информации в личном кабинете пользователя",
        tags=["Пользователь", "Личный кабинет пользователя"],
        responses={
            200: openapi.Response(
                "Информация обновлена",
                account_serializers.AccountUpdateSerializers,
            ),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление своего профиля самим пользователем",
        tags=["Пользователь", "Личный кабинет пользователя"],
        responses={
            200: openapi.Response("профиль успешно удалён"),
            401: openapi.Response("Не аутентифицированный"),
        },
    ),
)
class AccountViewSet(PersonalAccount):
    queryset = CustomerUser.objects.all()
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
