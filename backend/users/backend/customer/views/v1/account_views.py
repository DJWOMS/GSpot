from base.views import PersonalAccount, BaseAccountViewSet
from customer.serializers import account_serializers
from customer.models import CustomerUser
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Личный кабинет пользователя',
        tags=['Пользователь', 'Личный кабинет пользователя'],
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
        tags=['Пользователь', 'Личный кабинет пользователя'],
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
        tags=['Пользователь', 'Личный кабинет пользователя'],
        responses={
            200: openapi.Response('профиль успешно удалён'),
            401: openapi.Response('Не аутентифицированный'),
        },
    ),
)
class AccountViewSet(BaseAccountViewSet):
    model = CustomerUser
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'put', 'delete')

    serializer_map = {
        'GET': account_serializers.AccountRetrieveSerializers,
        'PUT': account_serializers.AccountUpdateSerializers,
        'DELETE': account_serializers.AccountRetrieveSerializers,
    }


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Изменение пароля пользователя',
        tags=['Пользователь', 'Личный кабинет пользователя'],
        responses={
            200: openapi.Response('Пароль успешно изменён'),
            401: openapi.Response('Не аутентифицированный'),
        },
    ),
)
class ChangePasswordViewSet(PersonalAccount):
    queryset = CustomerUser.objects.all()
    http_method_names = ['post']

    serializer_map = {
        'default': account_serializers.ChangePasswordRetUpdSerializers,
        'post': account_serializers.ChangePasswordRetUpdSerializers,
    }

    permission_map = {'default': [IsAuthenticated], 'post': [IsAuthenticated]}
