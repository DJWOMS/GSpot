from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from administrator.serializers.v1.employee_crud import EmployeeCreateUpdateSerializer
from base.views import PartialUpdateMixin
from common.permissions.permissons import CompanyOwnerPerm
from developer.models import CompanyUser
from developer.permissions import CompanyOwnerEmployeePerm
from developer.serializers.v1.employee_crud import (
    DeveloperEmployeeListSerializer,
    DeveloperEmployeeDetailSerializer,
    DeveloperEmployeeCreateUpdateSerializer,
)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_description='Создать сотрудника компании',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            201: openapi.Response(
                'Личная информация сотрудника', DeveloperEmployeeCreateUpdateSerializer
            ),
            400: openapi.Response('Данные не валидны'),
            403: openapi.Response('Отсутствуют права на создание сотрудника компании'),
        },
    ),
)
@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Перечень сотрудников компании',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            200: openapi.Response(
                'Личная информация сотрудника', DeveloperEmployeeCreateUpdateSerializer(many=True)
            ),
            403: openapi.Response('Отсутствуют права на просмотр списка сотрудников компании'),
        },
    ),
)
class DeveloperEmployeeListView(generics.ListCreateAPIView):
    permission_classes = [CompanyOwnerPerm]

    def get_queryset(self):
        return CompanyUser.objects.filter(company=self.request.user.company_owner).exclude(
            id=self.request.user.id
        )

    def perform_create(self, serializer):
        serializer.save(
            company=self.request.user.company,
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeveloperEmployeeListSerializer
        elif self.request.method == 'POST':
            return DeveloperEmployeeCreateUpdateSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Подробные данные о сотруднике компании',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            200: openapi.Response(
                'Личная информация сотрудника', DeveloperEmployeeCreateUpdateSerializer
            ),
            403: openapi.Response(
                'Отсутствуют права на получение подробных данных о сотруднике компании'
            ),
            404: openapi.Response('Сотрудник не найден'),
        },
    ),
)
@method_decorator(
    name='put',
    decorator=swagger_auto_schema(
        operation_description='Изменить данные о сотруднике компании',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            200: openapi.Response(
                'Личная информация сотрудника', DeveloperEmployeeCreateUpdateSerializer
            ),
            400: openapi.Response('Данные не валидны'),
            403: openapi.Response('Отсутствуют права на изменение данных о сотруднике компании'),
            404: openapi.Response('Сотрудник не найден'),
        },
    ),
)
@method_decorator(
    name='delete',
    decorator=swagger_auto_schema(
        operation_description='Удалить сотрудника компании',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            204: openapi.Response(
                'Сотрудник компании удален',
            ),
            403: openapi.Response('Отсутствуют права на удаление сотрудника компании'),
            404: openapi.Response('Администратор не найден'),
        },
    ),
)
class DeveloperEmployeeDetailView(PartialUpdateMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CompanyOwnerEmployeePerm]
    http_method_names = ['put', 'post', 'get']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return CompanyUser.objects.none()
        return CompanyUser.objects.filter(company=self.request.user.company_owner).exclude(
            id=self.request.user.id
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeveloperEmployeeDetailSerializer
        elif self.request.method == 'PUT':
            return EmployeeCreateUpdateSerializer
