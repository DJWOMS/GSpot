from administrator.serializers.v1.customer_seriallizers import (
    CustomerBlockSerializer,
    CustomerListSerializer,
    CustomerRetrieveSerializer,
    CustomerUnblockSerializer,
)
from base.paginations import BasePagination
from common.permissions.permissons import IsAdminScopeUserPerm
from customer.models import CustomerUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

list_schema = swagger_auto_schema(
    operation_description="Получить список пользователей",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Список пользователей", CustomerListSerializer(many=True)),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

retrieve_schema = swagger_auto_schema(
    operation_description="Детальный просмотр пользователя",
    tags=["Администратор", "Личный кабинет администратора"],
    responses={
        200: openapi.Response("Пользователь", CustomerRetrieveSerializer),
        401: openapi.Response("Не аутентифицированный пользователь"),
        403: openapi.Response("Отсутствуют права на просмотр"),
    },
)

unblock_schema = swagger_auto_schema(
    operation_description="Разблокировка пользователя",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)

block_schema = swagger_auto_schema(
    operation_description="Блокировка пользователя",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        201: openapi.Response("Успешно"),
        400: openapi.Response("Данные не валидны"),
        403: openapi.Response("Отсутствуют права на редактирование"),
    },
)

destroy_schema = swagger_auto_schema(
    operation_description="Удалить пользователя",
    tags=["Администратор", "Административная панель владельца"],
    responses={
        204: openapi.Response("Пользователь удалён"),
        403: openapi.Response("Отсутствуют права на редактирование"),
        404: openapi.Response("Пользователь не найден"),
    },
)


class CustomerListView(ModelViewSet):
    queryset = CustomerUser.objects.all()
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAdminScopeUserPerm]
    filter_backends = [filters.SearchFilter]
    search_fields = ["email", "phone"]
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CustomerRetrieveSerializer
        if self.action == "list":
            return CustomerListSerializer
        if self.action == "block":
            return CustomerBlockSerializer
        if self.action == "unblock":
            return CustomerUnblockSerializer

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
        customer: CustomerUser = self.get_object()
        serializer = CustomerBlockSerializer(
            data=request.data,
            context={
                "customer": customer,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, customer=customer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    @unblock_schema
    def unblock(self, request, pk):
        customer: CustomerUser = self.get_object()
        serializer = CustomerUnblockSerializer(
            data=request.data,
            context={
                "customer": customer,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user, customer=customer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
