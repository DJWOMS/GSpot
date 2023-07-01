from base.views import PersonalAccount, PartialUpdateMixin
from developer.models import CompanyUser
from developer.serializers import account_serializers
from common.permissions.permissons import IsCompanyScopeUserPerm

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
class AccountViewSet(PartialUpdateMixin, ModelViewSet):
    queryset = CompanyUser.objects.all()
    permission_classes = (IsCompanyScopeUserPerm,)
    http_method_names = ('get', 'put', 'delete',)

    serializer_map = {
        'GET': account_serializers.AccountRetrieveSerializers,
        'PUT': account_serializers.AccountUpdateSerializers,
    }

    def get_serializer_class(self):
        method = self.request.method
        return self.serializer_map.get(method)


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
