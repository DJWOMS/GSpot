from base.models import BaseAbstractUser
from common.permissions.user_permission_class import UserPermissionClass
from common.serializers.v1.mixed_account_retrieve_serializer import (
    MixedAccountRetrieveSerializer,
)
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
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
    permission_map = UserPermissionClass.get_permission_map()

    def create(self, request):
        uuid_list = request.data.get('uuid_list', [])
        users = BaseAbstractUser.objects.filter(uuid__in=uuid_list)
        if users:
            serializer = MixedAccountRetrieveSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
