from base.views import PersonalAccount
from developer.models import CompanyUser
from developer.serializers import account_serializers
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Личный кабинет пользователя',
        tags=['Разработчик', 'Личный кабинет'],
        responses={
            200: openapi.Response(
                'Личная информация пользователя', account_serializers.AccountRetrieveSerializers
            ),
            403: openapi.Response('Нет права для выполнения запроса'),
        },
    ),
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_description='Изменение информации в личном кабинете пользователя',
        tags=['Разработчик', 'Личный кабинет'],
        responses={
            200: openapi.Response(
                'Информация обновлена', account_serializers.AccountUpdateSerializers
            ),
            403: openapi.Response('Нет права для выполнения запроса'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удаление своего профиля самим пользователем',
        tags=['Разработчик', 'Личный кабинет'],
        responses={
            200: openapi.Response('Ваш профиль успешно удалён'),
            403: openapi.Response('Нет права для выполнения запроса'),
        },
    ),
)
class AccountViewSet(PersonalAccount):
    queryset = CompanyUser.objects.all()
    http_method_names = ['get', 'put', 'delete']

    serializer_map = {
        'default': account_serializers.AccountRetrieveSerializers,
        'retrieve': account_serializers.AccountRetrieveSerializers,
        'partial_update': account_serializers.AccountUpdateSerializers,
        'destroy': account_serializers.AccountRetrieveSerializers,
    }

    permission_map = {
        'default': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
    }


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Изменение пароля пользователя',
        tags=['Разработчик', 'Личный кабинет'],
        responses={
            201: openapi.Response('Ваш пароль успешно изменён'),
            403: openapi.Response('Нет права для выполнения запроса'),
        },
    ),
)
class ChangePasswordViewSet(PersonalAccount):
    queryset = CompanyUser.objects.all()
    http_method_names = ['post']

    serializer_map = {
        'default': account_serializers.ChangePasswordRetUpdSerializers,
        'post': account_serializers.ChangePasswordRetUpdSerializers,
    }

    permission_map = {'default': [IsAuthenticated], 'post': [IsAuthenticated]}
