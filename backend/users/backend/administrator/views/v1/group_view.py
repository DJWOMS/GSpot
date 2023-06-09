from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from administrator.serializers.v1 import AdminGroupSerializer
from administrator.models import AdminGroup
from base.views import PartialUpdateMixin


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_description='Список групп администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Список групп администраторов', AdminGroupSerializer(many=True)),
            403: openapi.Response('Отсутствуют права на просмотр списка групп администраторов'),
        },
    ),
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Детальное представление группы администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            200: openapi.Response('Группа администраторов', AdminGroupSerializer),
            403: openapi.Response('Отсутствуют права на детальный просмотр группы администратора'),
            404: openapi.Response('Группа администраторов не найдена'),
        },
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Добавить группу администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            201: openapi.Response('Группа администраторов', AdminGroupSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на создание группы администраторов'),
        },
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_description='Изменить группу администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            201: openapi.Response('Группа администраторов', AdminGroupSerializer),
            400: openapi.Response('Невалидные данные'),
            403: openapi.Response('Отсутствуют права на изменение группы администраторов'),
            404: openapi.Response('Группа администраторов не найдена'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удалить группу администраторов',
        tags=['Администратор', 'Административная панель владельца'],
        responses={
            204: openapi.Response('Группа администраторов'),
            403: openapi.Response('Отсутствуют права на удаление группы администраторов'),
            404: openapi.Response('Группа администраторов не найдена'),
        },
    ),
)
class AdminGroupViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    permission_classes = [IsAuthenticated]
    queryset = AdminGroup.objects.all()
    serializer_class = AdminGroupSerializer
