from administrator.models import Admin
from administrator.serializers import account_serializers as admin_account_serializers
from base.models import BaseAbstractUser
from base.views import PersonalAccount
from customer.models import CustomerUser
from customer.serializers import account_serializers as customer_account_serializers
from developer.models import CompanyUser
from developer.serializers import account_serializers as developer_account_serializers
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
            ),
            401: openapi.Response("Не аутентифицированный пользователь"),
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
                # account_serializers.AccountUpdateSerializers,
            ),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удаление своего профиля самим пользователем",
        tags=["Пользователь", "Личный кабинет пользователя"],
        responses={
            200: openapi.Response("профиль пользователя успешно удалён"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
class AccountViewSet(PersonalAccount):
    http_method_names = ["get", "put", "delete"]
    admin_serializer_map = {
        "default": admin_account_serializers.AccountRetrieveSerializers,
        "retrieve": admin_account_serializers.AccountRetrieveSerializers,
        "partial_update": admin_account_serializers.AccountUpdateSerializers,
        "destroy": admin_account_serializers.AccountRetrieveSerializers,
    }
    developer_serializer_map = {
        "default": developer_account_serializers.AccountRetrieveSerializers,
        "retrieve": developer_account_serializers.AccountRetrieveSerializers,
        "partial_update": developer_account_serializers.AccountUpdateSerializers,
        "destroy": developer_account_serializers.AccountRetrieveSerializers,
    }
    customer_serializer_map = {
        "default": customer_account_serializers.AccountRetrieveSerializers,
        "retrieve": customer_account_serializers.AccountRetrieveSerializers,
        "partial_update": customer_account_serializers.AccountUpdateSerializers,
        "destroy": customer_account_serializers.AccountRetrieveSerializers,
    }
    permission_map = {
        "default": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }

    def get_queryset(self):
        role = self.request.user._meta.app_label

        if role == 'administrator':
            return Admin.objects.all()
        elif role == 'customer':
            return CustomerUser.objects.all()
        elif role == 'developer':
            return CompanyUser.objects.all()

        return BaseAbstractUser.objects.none()

    def get_serializer_class(self):
        role = self.request.user._meta.app_label
        serializers_by_role = {
            'administrator': self.admin_serializer_map,
            'developer': self.developer_serializer_map,
            'customer': self.customer_serializer_map,
        }
        serializer_map = serializers_by_role[role]
        return serializer_map.get(self.action, serializer_map["default"])
