from administrator.serializers.v1.company_serializer import (
    CompanyBlockSerializer,
    CompanyListSerializer,
    CompanyRetrieveSerializer,
    CompanyUnblockSerializer,
)
from base.paginations import BasePagination
from common.permissions.permissons import IsAdminScopeUserPerm
from developer.models import Company, CompanyUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

list_schema = swagger_auto_schema(
    operation_description="Получить список компаний",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Список компаний", CompanyListSerializer(many=True)),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

retrieve_schema = swagger_auto_schema(
    operation_description="Детальный просмотр компании",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Компания", CompanyRetrieveSerializer),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

unblock_schema = swagger_auto_schema(
    operation_description="Разблокировка компании",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)

block_schema = swagger_auto_schema(
    operation_description="Блокировка компании",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
    },
)

destroy_schema = swagger_auto_schema(
    operation_description="Удалить компанию",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        204: openapi.Response("Пользователь удалён"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)


class CompanyListView(ModelViewSet):
    queryset = Company.objects.all()
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAdminScopeUserPerm]
    filter_backends = [filters.SearchFilter]
    pagination_class = BasePagination
    search_fields = [
        "email",
        "phone",
        "id",
        "title",
        "created_by",
    ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CompanyRetrieveSerializer
        if self.action == "list":
            return CompanyListSerializer
        if self.action == "block":
            return CompanyBlockSerializer
        if self.action == "unblock":
            return CompanyUnblockSerializer

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
        company: CompanyUser = self.get_object()
        serializer = CompanyBlockSerializer(
            data=request.data,
            context={
                "company": company,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, company=company)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    @unblock_schema
    def unblock(self, request, pk):
        company: CompanyUser = self.get_object()
        serializer = CompanyUnblockSerializer(
            data=request.data,
            context={
                "company": company,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, company=company)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
