from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from base.views import BaseAdminSuperUserViewSet

from common.models import ContactType
from common.serializers.v1.contacttype_serializer import ContactTypeSerializer


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получить все данные типов контакта",
        tags=[
            "Тип контакта",
        ],
        responses={
            200: openapi.Response("Список типов контакта", ContactTypeSerializer(many=True)),
            403: openapi.Response(
                "Список типов контакта доступен только авторизованным пользователям"
            ),
        },
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Создать запись о типе контактанта по идентификатору",
        tags=[
            "Тип контакта",
        ],
        responses={
            201: openapi.Response("Запись успешно создана", ContactTypeSerializer),
            400: openapi.Response("Входные данные не валидны"),
            403: openapi.Response("Создание записи в БД доступна только администратору"),
        },
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Обновить определенную запись о типе контактанта по идентификатору",
        tags=[
            "Тип контакта",
        ],
        responses={
            200: openapi.Response("Запись успешно обновлена", ContactTypeSerializer),
            400: openapi.Response("Входные данные не валидны"),
            403: openapi.Response("Изменение записи в БД доступна только администратору"),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Удалить определенную запись о типе контактантов по идентификатору",
        tags=[
            "Тип контакта",
        ],
        responses={
            204: openapi.Response("Запись успешно удалена"),
            403: openapi.Response("Удаление записи из БД доступна только администратору"),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    ),
)
class ContactTypeViewSet(BaseAdminSuperUserViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer

    @swagger_auto_schema(
        operation_description="Получить определенные данные о типе контактантов по id",
        tags=[
            "Тип контакта",
        ],
        responses={
            200: openapi.Response("Список типов контакта", ContactTypeSerializer),
            403: openapi.Response(
                "Список типов контактов доступен только авторизованным пользователям"
            ),
            404: openapi.Response("Записи с таким ID не существует"),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
