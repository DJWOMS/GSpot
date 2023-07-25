from administrator.models import Admin
from administrator.serializers import account_serializers as admin_account_serializers
from customer.models import CustomerUser
from customer.serializers import account_serializers as customer_account_serializers
from developer.models import CompanyUser
from developer.serializers import account_serializers as developer_account_serializers
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
class AccountSingleUserViewSet(viewsets.ViewSet):
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = {
            'administrator': Admin.objects.all(),
            'developer': CompanyUser.objects.all(),
            'customer': CustomerUser.objects.all(),
        }

        role = self.request.user._meta.app_label
        return qs.get(role, [])

    def retrieve(self):
        user = self.get_object()
        if user:
            serializers_by_role = {
                'administrator': self.admin_serializer_map,
                'developer': self.developer_serializer_map,
                'customer': self.customer_serializer_map,
            }
            role = user._meta.app_label
            serializer_map = serializers_by_role.get(role)
            if serializer_map is None:
                return Response(status=404)

            serializer = serializer_map['default'](user)
            return Response(serializer.data)
        else:
            return Response(status=404)
