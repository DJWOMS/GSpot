from base.paginations import BasePagination
from common.permissions import permissons
from common.services.notify.notify import Notify
from customer.models import CustomerUser, FriendShipRequest
from customer.serializers.v1 import friends_serializer
from customer.services.get_query_friend import get_queryset_for_delete_user
from django.db import transaction
from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.broker.message import FriendAddedMessage


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получение списка пользователей для добавления в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Список пользователей", friends_serializer.UserSerializer),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Получение пользователя для детального просмотра",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Пользователь", friends_serializer.UserRetrieveSerializer),
            404: openapi.Response("Не найден пользователь"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="add_friend",
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description="Отправка запроса для добавления в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Пользователь добавлен"),
            400: openapi.Response("Данные не валидны"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
class AddFriendsView(viewsets.ModelViewSet):
    permission_classes = [
        permissons.IsCustomerScopeUserPerm,
    ]
    serializer_class = friends_serializer.UserSerializer
    filter_backends = [filters.SearchFilter]
    serializer_classes_by_action = {
        "list": friends_serializer.UserSerializer,
        "retrieve": friends_serializer.UserRetrieveSerializer,
    }
    search_fields = ("username",)
    http_method_names = ["get", "post", "add_friend"]
    pagination_class = BasePagination
    lookup_url_kwarg = "user_id"

    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        friends = self.request.user.friends.all() | CustomerUser.objects.filter(
            friends=self.request.user,
        )
        return CustomerUser.objects.filter(is_active=True, is_banned=False).exclude(
            Q(id=self.request.user.id) | Q(id__in=friends.values_list("id", flat=True)),
        )

    @action(methods=["post"], detail=True, url_path="add-friend", url_name="add_friend")
    def add_friend(self, request, user_id):
        get_object = self.get_object()
        message = FriendAddedMessage(user=get_object, sender_user=self.request.user)
        Notify().send_notify(
            message=message,
        )
        with transaction.atomic():
            instance = FriendShipRequest(
                sender=self.request.user,
                receiver=get_object,
                status='REQUESTED',
            )
            instance.save()
            return Response(status=status.HTTP_200_OK)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получение списка запросов на добавление в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Список запросов", friends_serializer.UserSerializer),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Просмотр пользователя на добавление в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Пользователь", friends_serializer.UserRetrieveSerializer),
            404: openapi.Response("Не найден пользователь"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description="Принятие запроса для добавления в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Запрос на добавление принят"),
            400: openapi.Response("Данные не валидны"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        request_body=friends_serializer.AddFriendSerializer,
        operation_description="Отклонение запроса для добавления в друзья",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Запрос на отклонение отправлен"),
            400: openapi.Response("Данные не валидны"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
class ListRetrieveAcceptRejectAddFriendsView(viewsets.ModelViewSet):
    permission_classes = [
        permissons.IsCustomerScopeUserPerm,
    ]
    serializer_classes_by_action = {
        "list": friends_serializer.UserSerializer,
        "retrieve": friends_serializer.UserRetrieveSerializer,
        "create": friends_serializer.AcceptAddFriendSerializer,
        "destroy": friends_serializer.RejectAddFriendSerializer,
    }
    filter_backends = [filters.SearchFilter]
    http_method_names = ["get", "post", "delete"]
    pagination_class = BasePagination
    lookup_url_kwarg = "user_id"

    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        requests_friend = FriendShipRequest.objects.filter(
            receiver_id=self.request.user.id,
            status="REQUESTED",
        ).values_list("sender", flat=True)
        return CustomerUser.objects.filter(is_active=True, is_banned=False, id__in=requests_friend)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(
                receiver_user=self.request.user,
                sender_user=self.get_object(),
            )
            return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(
                receiver_user=self.request.user,
                sender_user=self.get_object(),
            )
            return Response(status=status.HTTP_200_OK)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Получение своего списка друзей для удаления",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Список друзей", friends_serializer.UserSerializer),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Детальный просмотр друга",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Пользователь", friends_serializer.UserRetrieveSerializer),
            404: openapi.Response("Не найден пользователь"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        request_body=friends_serializer.DeleteFriendSerializer,
        operation_description="Удаление друзей из списка",
        tags=["Пользователь", "Друзья"],
        responses={
            200: openapi.Response("Пользователь удалён"),
            400: openapi.Response("Данные не валидны"),
            401: openapi.Response("Не аутентифицированный пользователь"),
        },
    ),
)
class ListRetrieveDestroyFriendsView(viewsets.ModelViewSet):
    permission_classes = [
        permissons.IsCustomerScopeUserPerm,
    ]
    filter_backends = [filters.SearchFilter]
    serializer_classes_by_action = {
        "list": friends_serializer.UserSerializer,
        "retrieve": friends_serializer.UserRetrieveSerializer,
    }
    http_method_names = ["get", "delete"]
    search_fields = ("username",)
    serializer_class = friends_serializer.UserRetrieveSerializer
    pagination_class = BasePagination
    lookup_url_kwarg = "user_id"

    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        friend = get_queryset_for_delete_user(self.request.user)
        return CustomerUser.objects.filter(is_active=True, is_banned=False, id__in=friend)

    def destroy(self, request, *args, **kwargs):
        serializer = friends_serializer.DeleteFriendSerializer(
            data=request.data,
            context=self.get_serializer_context(),
        )
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(
                receiver_user=self.request.user,
                sender_user=self.get_object(),
            )
            return Response(status=status.HTTP_200_OK)
