from django.db import transaction
from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, filters, status
from rest_framework.response import Response
from common.permissions.permissons import IsCustomerScopeUserPerm
from customer.models import CustomerUser, FriendShipRequest
from customer.serializers.v1 import friends_serializer
from customer.services.get_query_friend import get_queryset_for_delete_user
from customer.services.pagination import PaginationFriend


class FriendsView(generics.ListCreateAPIView):
    permission_classes = [
        IsCustomerScopeUserPerm,
    ]
    serializer_class = friends_serializer.UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('username',)
    http_method_names = ['get', 'post']
    pagination_class = PaginationFriend

    def get_queryset(self):
        requests_friend = FriendShipRequest.objects.filter(
            receiver_id=self.request.user.id, status='REQUESTED'
        ).values_list('sender', flat=True)
        return CustomerUser.objects.filter(is_active=True, is_banned=False, id__in=requests_friend)

    def create(self, request, *args, **kwargs):
        serializer = self.get_create_serializer()(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(
                receiver_user=self.request.user,
                sender_user=serializer.validated_data['sender_user'],
            )
            headers = self.get_success_headers(serializer.data)
            return Response(status=status.HTTP_200_OK, headers=headers)

    @staticmethod
    def get_create_serializer():
        raise NotImplementedError


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Получение списка пользователей для добавления в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Список пользователей', friends_serializer.UserSerializer),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description='Отправка запроса для добавления в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Пользователь добавлен'),
            400: openapi.Response('Данные не валидны'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class AddFriendsView(FriendsView):
    def get_queryset(self):
        friends = self.request.user.friends.all() | CustomerUser.objects.filter(
            friends=self.request.user
        )
        return CustomerUser.objects.filter(is_active=True, is_banned=False).exclude(
            Q(id=self.request.user.id) | Q(id__in=friends.values_list('id', flat=True))
        )

    def create(self, request, *args, **kwargs):
        serializer = friends_serializer.AddFriendSerializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(user=self.request.user, user_add=serializer.validated_data['user_add'])
            headers = self.get_success_headers(serializer.data)
            send_message_in_rabbitmq = True
            if send_message_in_rabbitmq:
                return Response(status=status.HTTP_200_OK, headers=headers)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Получение списка запросов на добавление в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Список запросов', friends_serializer.UserSerializer),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description='Принятие запроса для добавления в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Запрос на добавление принят'),
            400: openapi.Response('Данные не валидны'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class AcceptAddFriendsView(FriendsView):
    @staticmethod
    def get_create_serializer():
        return friends_serializer.AcceptAddFriendSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Получение списка запросов на добавление в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Список запросов', friends_serializer.UserSerializer),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description='Отклонение запроса для добавления в друзья',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Запрос на отклонение отправлен'),
            400: openapi.Response('Данные не валидны'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class RejectAddFriendsView(FriendsView):
    @staticmethod
    def get_create_serializer():
        return friends_serializer.RejectAddFriendSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_description='Получение своего списка друзей для удаления',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Список друзей', friends_serializer.UserSerializer),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description='Удаление друзей из списка',
        tags=['Пользователь', 'Друзья'],
        responses={
            200: openapi.Response('Запрос на удаление отправлен'),
            400: openapi.Response('Данные не валидны'),
            401: openapi.Response('Не аутентифицированный пользователь'),
        },
    ),
)
class DeleteFriendsView(FriendsView):
    def get_queryset(self):
        friend = get_queryset_for_delete_user(self.request.user)
        return CustomerUser.objects.filter(is_active=True, is_banned=False, id__in=friend)

    @staticmethod
    def get_create_serializer():
        return friends_serializer.DeleteFriendSerializer
