from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from base.views import BaseAdminSuperUserViewSet

from common.models import Country
from common.serializers.v1.country_serializer import CountrySerializer


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получить список стран",
        tags=[
            "Список стран",
        ],
        responses={
            200: openapi.Response("Список стран", CountrySerializer(many=True)),
            403: openapi.Response("Список стран доступен только авторизованным пользователям"),
        },
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Создать запись о стране в базе данных по id",
        tags=[
            "Список стран",
        ],
        responses={
            201: openapi.Response("Запись успешно создана", CountrySerializer),
            400: openapi.Response("Входные данные не валидны"),
            403: openapi.Response("Создание записи в БД доступна только администратору"),
        },
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Обновить запись о стране в базе данных по id",
        tags=[
            "Список стран",
        ],
        responses={
            200: openapi.Response("Запись успешно обновлена"),
            400: openapi.Response("Входные данные не валидны"),
            403: openapi.Response("Создание записи в БД доступна только администратору"),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удалить запись о стране в базе данных по id",
        tags=[
            "Список стран",
        ],
        responses={
            204: openapi.Response("Запись успешно удалена"),
            403: openapi.Response("Удлаение записи в БД доступна только администратору"),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    ),
)
class CountryViewSet(BaseAdminSuperUserViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @swagger_auto_schema(
        operation_description="Получить уникальную запись по id",
        tags=[
            "Список стран",
        ],
        responses={
            200: openapi.Response("Список стран", CountrySerializer),
            403: openapi.Response(
                "Список стран содержимого доступен только авторизованным пользователям"
            ),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
