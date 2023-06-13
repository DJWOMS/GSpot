from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from administrator.models import BlockReason
from administrator.serializers.customer_seriallizers import (
    CustomerListSerializer,
    CustomerBlockSerializer,
    CustomerRetrieveSerializer,
)
from common.permissions.permissons import IsAdminScopeUserPerm
from customer.models import CustomerUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_description='Получить список пользователей',
        tags=['Администратор', 'Личный кабинет администратора'],
        responses={
            200: openapi.Response('Список пользователей', CustomerListSerializer(many=True)),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='unblock',
    decorator=swagger_auto_schema(
        operation_description='Блокировка / Разблокировка пользователя',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Успешно'),
            400: openapi.Response('Данные не валидны'),
            403: openapi.Response('Отсутствуют права на редактирование'),
        },
    ),
)
@method_decorator(
    name='block',
    decorator=swagger_auto_schema(
        operation_description='Блокировка пользователя',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Успешно'),
            400: openapi.Response('Данные не валидны'),
            403: openapi.Response('Отсутствуют права на редактирование'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удалить пользователя',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Пользователь удалён'),
            403: openapi.Response('Отсутствуют права на редактирование'),
        },
    ),
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
        else:
            return CustomerListSerializer

    def block(self, request, pk):
        context = {'pk': pk, 'creator': request.user.id}
        serializer = CustomerBlockSerializer(data=request.data, context=context)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def unblock(self, _request, pk):
        user = CustomerUser.objects.get(pk=pk)
        user.is_banned = False
        user.save()
        return Response(status=status.HTTP_200_OK)
