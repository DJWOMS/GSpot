from base.views import PartialUpdateMixin
from developer.models import DeveloperGroup
from developer.serializers.v1 import DeveloperGroupSerializer
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Список групп разработчиков",
        tags=["Разработчик", "Административная панель разработчика"],
        responses={
            200: openapi.Response(
                "Список групп разработчиков",
                DeveloperGroupSerializer(many=True),
            ),
            403: openapi.Response("Отсутствуют права на просмотр списка групп разработчиков"),
        },
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Детальное представление группы разработчиков",
        tags=["Разработчик", "Административная панель разработчика"],
        responses={
            200: openapi.Response("Группа разработчиков", DeveloperGroupSerializer),
            403: openapi.Response("Отсутствуют права на просмотр группы разработчика"),
            404: openapi.Response("Группа разработчиков не найдена"),
        },
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Добавить группу разработчика",
        tags=["Разработчик", "Административная панель разработчика"],
        responses={
            201: openapi.Response("Группа разработчика", DeveloperGroupSerializer),
            400: openapi.Response("Невалидные данные"),
            403: openapi.Response("Отсутствуют права на создание группы разработчиков"),
        },
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Изменить группу разработчика",
        tags=["Разработчик", "Административная панель разработчика"],
        responses={
            200: openapi.Response("Группа разработчика", DeveloperGroupSerializer),
            400: openapi.Response("Невалидные данные"),
            403: openapi.Response("Отсутствуют права на изменение группы разработчика"),
            404: openapi.Response("Группа разработчика не найдена"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удалить группу разработчиков",
        tags=["Разработчик", "Административная панель разработчика"],
        responses={
            204: openapi.Response("Группа разработчика"),
            403: openapi.Response("Отсутствуют права на удаление группы разработчика"),
            404: openapi.Response("Группа разработчика не найдена"),
        },
    ),
)
class DeveloperGroupViewSet(PartialUpdateMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated]
    queryset = DeveloperGroup.objects.all()
    serializer_class = DeveloperGroupSerializer
