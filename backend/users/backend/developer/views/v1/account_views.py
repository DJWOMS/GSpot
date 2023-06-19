from base.views import PersonalAccount
from developer.models import CompanyUser
from developer.serializers import account_serializers

from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Личный кабинет пользователя',
        tags=['Разработчик', 'Личный кабинет разработчика'],
        responses={
            200: openapi.Response(
                'Личная информация пользователя',
                account_serializers.AccountRetrieveSerializers
            ),
            401: openapi.Response('Не аутентифицированный'),
        },
    ),
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_description='Изменение информации в личном кабинете пользователя',
        tags=['Разработчик', 'Личный кабинет разработчика'],
        responses={
            200: openapi.Response(
                'Информация обновлена',
                account_serializers.AccountUpdateSerializers
            ),
            401: openapi.Response('Не аутентифицированный'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удаление своего профиля самим пользователем',
        tags=['Разработчик', 'Личный кабинет разработчика'],
        responses={
            200: openapi.Response('профиль успешно удалён'),
            401: openapi.Response('Не аутентифицированный'),
        },
    ),
)
class AccountViewSet(ModelViewSet):
    model = CompanyUser
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'put', 'delete',)

    serializer_map = {
        'GET': account_serializers.AccountRetrieveSerializers,
        'UPDATE': account_serializers.AccountUpdateSerializers,
        'DELETE': account_serializers.AccountRetrieveSerializers,
    }

    def get_serializer_class(self):
        action = self.request.method
        return self.serializer_map.get(action)

    def get_object(self):
        object_ = self.request.user

        if isinstance(self.request.user, self.model):
            return object_
        raise NotFound()


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Изменение пароля пользователя',
        tags=['Разработчик', 'Личный кабинет разработчика'],
        responses={
            200: openapi.Response('пароль успешно изменён'),
            401: openapi.Response('Не аутентифицированный'),
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
