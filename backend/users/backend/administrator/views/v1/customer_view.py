from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from administrator.serializers.customer_seriallizers import (
    CustomerListSerializer,
    CustomerBlockSerializer,
    CustomerRetrieveSerializer,
    CustomerRequestBlockSerializer,
)
from common.permissions.permissons import IsAdminScopeUserPerm
from customer.models import CustomerUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

list_schema = swagger_auto_schema(
    operation_description='Получить список пользователей',
    tags=['Администратор', 'Личный кабинет администратора'],
    responses={
        200: openapi.Response('Список пользователей', CustomerListSerializer(many=True)),
        401: openapi.Response('Не аутентифицированный пользователь'),
    },
)

unblock_schema = swagger_auto_schema(
    operation_description='Разблокировка пользователя',
    tags=['Администратор', 'Административная панель владельца'],
    responses={
        200: openapi.Response('Успешно'),
        400: openapi.Response('Данные не валидны'),
        403: openapi.Response('Отсутствуют права на редактирование'),
    },
)

block_schema = swagger_auto_schema(
    operation_description='Блокировка пользователя',
    tags=['Администратор', 'Административная панель владельца'],
    responses={
        200: openapi.Response('Успешно'),
        400: openapi.Response('Данные не валидны'),
        403: openapi.Response('Отсутствуют права на редактирование'),
    },
)

destroy_schema = swagger_auto_schema(
    operation_description='Удалить пользователя',
    tags=['Администратор', 'Административная панель владельца'],
    responses={
        200: openapi.Response('Пользователь удалён'),
        403: openapi.Response('Отсутствуют права на редактирование'),
    },
)


class CustomerListView(ModelViewSet):
    queryset = CustomerUser.objects.all()
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAdminScopeUserPerm]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'phone']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CustomerRetrieveSerializer
        if self.action == 'block':
            return CustomerRequestBlockSerializer
        if self.action == 'list':
            return CustomerListSerializer
        return None

    @list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @destroy_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @block_schema
    def block(self, request, pk):
        block_customer = self.get_object()
        serializer = CustomerBlockSerializer(
            data=request.data,
            context={
                'user': block_customer,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    @unblock_schema
    def unblock(self, _request, pk):
        user = CustomerUser.objects.get(pk=pk)
        user.is_banned = False
        user.save()
        return Response(status=status.HTTP_200_OK)
