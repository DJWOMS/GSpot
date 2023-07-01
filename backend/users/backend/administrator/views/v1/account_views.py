from base.views import PersonalAccount, PartialUpdateMixin
from administrator.models import Admin
from administrator.serializers import account_serializers
from common.permissions.permissons import IsAdminScopeUserPerm

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Личный кабинет пользователя',
        tags=['Администратор', 'Личный кабинет администратора'],
        responses={
            200: openapi.Response(
                'Личная информация администратора',
                account_serializers.AccountRetrieveSerializers
            ),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        operation_description='Изменение информации в личном кабинете пользователя',
        tags=['Администратор', 'Личный кабинет администратора'],
        responses={
            200: openapi.Response(
                'Личная информация администратора',
                account_serializers.AccountUpdateSerializers
            ),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Удаление профиля администратора',
        tags=['Администратор', 'Личный кабинет администратора'],
        responses={
            204: openapi.Response('Профиль администратора успешно удалён'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class AccountViewSet(PartialUpdateMixin, ModelViewSet):
    permission_classes = (IsAdminScopeUserPerm,)
    http_method_names = ['get', 'put', 'delete']

    serializer_map = {
        'GET': account_serializers.AccountRetrieveSerializers,
        'PUT': account_serializers.AccountUpdateSerializers,
    }

    def get_serializer_class(self):
        method = self.request.method
        return self.serializer_map.get(method)

    def get_object(self):
        return self.request.user


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Изменение пароля пользователя',
        tags=['Администратор', 'Личный кабинет администратора'],
        responses={
            200: openapi.Response('Пароль успешно изменён'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class ChangePasswordViewSet(PersonalAccount):
    queryset = Admin.objects.all()
    http_method_names = ['post']

    serializer_map = {
        'default': account_serializers.ChangePasswordRetUpdSerializers,
        'post': account_serializers.ChangePasswordRetUpdSerializers,
    }

    permission_map = {'default': [IsAuthenticated], 'post': [IsAuthenticated]}
