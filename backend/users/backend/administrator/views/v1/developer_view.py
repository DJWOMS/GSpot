from administrator.serializers.v1.developer_serializer import (
    DeveloperBlockSerializer,
    DeveloperListSerializer,
    DeveloperRetrieveSerializer,
    DeveloperUnblockSerializer,
)
from base.paginations import BasePagination
from common.permissions.permissons import IsAdminScopeUserPerm
from developer.models import CompanyUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

list_schema = swagger_auto_schema(
    operation_description="Получить список разработчиков",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Список разработчиков", DeveloperListSerializer(many=True)),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

retrieve_schema = swagger_auto_schema(
    operation_description="Детальный просмотр разработчика",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Пользователь", DeveloperRetrieveSerializer),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

unblock_schema = swagger_auto_schema(
    operation_description="Разблокировка разработчика",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)

block_schema = swagger_auto_schema(
    operation_description="Блокировка разработчика",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
    },
)

destroy_schema = swagger_auto_schema(
    operation_description="Удалить разработчика",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        204: openapi.Response("Пользователь удалён"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)


class DeveloperListView(ModelViewSet):
    queryset = CompanyUser.objects.all()
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAdminScopeUserPerm]
    filter_backends = [filters.SearchFilter]
    pagination_class = BasePagination
    search_fields = [
        "email",
        "phone",
        "company__id",
        "company__title",
    ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DeveloperRetrieveSerializer
        if self.action == "list":
            return DeveloperListSerializer
        if self.action == "block":
            return DeveloperBlockSerializer
        if self.action == "unblock":
            return DeveloperUnblockSerializer

    @list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @retrieve_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @destroy_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @block_schema
    def block(self, request, pk):
        company_user: CompanyUser = self.get_object()
        serializer = DeveloperBlockSerializer(
            data=request.data,
            context={
                "company_user": company_user,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, company_user=company_user)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    @unblock_schema
    def unblock(self, request, pk):
        company_user: CompanyUser = self.get_object()
        serializer = DeveloperUnblockSerializer(
            data=request.data,
            context={
                "company_user": company_user,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, company_user=company_user)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
