from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from administrator.serializers.v1 import AdminPermissionSerializer
from administrator.models import AdminPermission
from base.views import PartialUpdateMixin


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_description='Список прав администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response(
                'Список прав администраторов', AdminPermissionSerializer(many=True)
            ),
            403: openapi.Response('Отсутствуют права на просмотр списка прав администраторов'),
        },
    ),
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Детальное представление прав администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Право администраторов', AdminPermissionSerializer),
            403: openapi.Response('Отсутствуют права просмотр права администратора'),
            404: openapi.Response('Право не найдено'),
        },
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Добавить право администратора',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            201: openapi.Response('Право администратора', AdminPermissionSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на создание права администраторов'),
        },
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_description='Изменить право администратора',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            201: openapi.Response('Право администратора', AdminPermissionSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на изменение права администратора'),
            404: openapi.Response('Право администратора не найдено'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удалить право администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            204: openapi.Response('Право администратора'),
            403: openapi.Response('Отсутствуют права на удаление права администратора'),
            404: openapi.Response('Право администраторов не найдено'),
        },
    ),
)
class AdminPermissionViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAuthenticated]
    queryset = AdminPermission.objects.all()
    serializer_class = AdminPermissionSerializer
