from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from base.views import PartialUpdateMixin
from developer.models import DeveloperPermission
from developer.serializers.v1 import DeveloperPermissionSerializer


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_description='Список прав разработчиков',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            200: openapi.Response(
                'Список прав разработчиков', DeveloperPermissionSerializer(many=True)
            ),
            403: openapi.Response('Отсутствуют права на просмотр списка прав разработчиков'),
        },
    ),
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Детальное представление прав разработчиков',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            200: openapi.Response('Право разработчика', DeveloperPermissionSerializer),
            403: openapi.Response('Отсутствуют права на детальный просмотр права разработчика'),
            404: openapi.Response('Право разработчика не найдено'),
        },
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Добавить право разработчика',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            201: openapi.Response('Право разработчика', DeveloperPermissionSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на создание права разработчиков'),
        },
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_description='Изменить право разработчика',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            201: openapi.Response('Право разработчика', DeveloperPermissionSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на изменение права разработчика'),
            404: openapi.Response('Право разработчика не найдено'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удалить право разработчика',
        tags=['Разработчик', 'Административная панель разработчика'],
        responses={
            204: openapi.Response('Право разработчика удалено'),
            403: openapi.Response('Отсутствуют права на удаление права разработчика'),
            404: openapi.Response('Право разработчика не найдено'),
        },
    ),
)
class DeveloperPermissionViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAuthenticated]
    queryset = DeveloperPermission.objects.all()
    serializer_class = DeveloperPermissionSerializer
