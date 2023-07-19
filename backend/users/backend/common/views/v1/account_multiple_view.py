from base.models import BaseAbstractUser
from common.serializers.v1.mixed_account_retrieve_serializer import (
    MixedAccountRetrieveSerializer,
)
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# @method_decorator(
#     name="retrieve",
#     decorator=swagger_auto_schema(
#         operation_description="Личный кабинет пользователя",
#         tags=["Пользователь", "Личный кабинет пользователя"],
#         responses={
#             200: openapi.Response(
#                 "Личная информация пользователя",
#                 #account_serializers.AccountRetrieveSerializers,
#             ),
#             401: openapi.Response("Не аутентифицированный пользователь"),
#         },
#     ),
# )
class AccountMultipleUsersViewSet(viewsets.ViewSet):
    permission_map = {
        "default": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }

    def create(self, request):
        uuid_list = request.data.get('uuid_list', [])
        users = BaseAbstractUser.objects.filter(uuid__in=uuid_list)
        if users:
            serializer = MixedAccountRetrieveSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
