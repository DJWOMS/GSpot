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
    name="create",
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
class AccountMultipleUsersViewSet(viewsets.ViewSet):
    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def get_users_queryset(self, users_uuid: list):
        administrators = Admin.objects.filter(id__in=users_uuid)
        customers = CustomerUser.objects.filter(id__in=users_uuid)
        developers = CompanyUser.objects.filter(id__in=users_uuid)
        return administrators, customers, developers

    def create(self, request):
        uuid_list = request.data.get('uuid_list', [])
        administrators, customers, developers = self.get_users_queryset(users_uuid=uuid_list)
        return Response(
            {
                'administrators': admin_account_serializers.AccountRetrieveSerializers(
                    administrators,
                    many=True,
                ).data,
                'developers': developer_account_serializers.AccountRetrieveSerializers(
                    developers,
                    many=True,
                ).data,
                'customers': customer_account_serializers.AccountRetrieveSerializers(
                    customers,
                    many=True,
                ).data,
            },
        )
