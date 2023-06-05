from django.db import transaction
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from customer.models import CustomerUser, FriendShipRequest
from customer.serializers.v1.friendship_serializer import FriendShipRequestSerializer
from utils.broker.message import FriendAddedMessage
from utils.broker.rabbitmq import RabbitMQ


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = FriendShipRequestSerializer
    http_method_names = ['post']

    def _get_friend(self, friend_id):
        try:
            friend = CustomerUser.objects.get(id=friend_id)
            return friend
        except CustomerUser.DoesNotExist:
            return Response({'error': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(operation_description='Отправить запрос на добавление в друзья', tags=['Друзья'])
    def add_friend(self, request, pk=None):
        user = request.user
        request_data = json.loads(request.data)
        friend_id = request_data['friend_id']
        friend = self._get_friend(friend_id)

        friend_request_exists = FriendShipRequest.objects.filter(sender=user, receiver=friend).exists()
        if friend_request_exists:
            return Response({'error': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            FriendShipRequest.objects.create(sender=user, receiver=friend)
            message = FriendAddedMessage(
                exchange_name='friend_added_exchange',
                routing_key='friend_added_queue',
                message={'friend_id': str(friend_id), "sender_id": str(user.id)}
            )
            with RabbitMQ() as rabbitmq:
                rabbitmq.send_message(message)
        return Response({'success': 'Friend request sent.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(operation_description='Принять запрос на добавление в друзья', tags=['Друзья'])
    def accept_friend_request(self, request, pk=None):
        user = request.user
        friend_id = request.data.get('friend_id')
        friend = self._get_friend(friend_id)
        if friend is None:
            return Response({'error': 'Friend not found.'}, status=status.HTTP_404_NOT_FOUND)
        friend_request = FriendShipRequest.objects.get(sender=friend, receiver=user)
        friend_request.status = FriendShipRequest.ACCEPTED
        friend_request.save()
        return Response({'success': 'Friend request accepted.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(operation_description='Отклонить запрос на добавление в друзья', tags=['Друзья'])
    def reject_friend_request(self, request, pk=None):
        user = request.user
        friend_id = request.data.get('friend_id')
        friend = self._get_friend(friend_id)
        if friend is None:
            return Response({'error': 'Friend not found.'}, status=status.HTTP_404_NOT_FOUND)
        friend_request = FriendShipRequest.objects.get(sender=friend, receiver=user)
        friend_request.status = FriendShipRequest.REJECTED
        friend_request.save()
        return Response({'success': 'Friend request rejected.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(operation_description='Удаление друга из списка друзей', tags=['Друзья'])
    def remove_friend(self, request, pk=None):
        user = request.user
        friend_id = request.data.get('friend_id')
        friend = self._get_friend(friend_id)
        if friend is None:
            return Response({'error': 'Friend not found.'}, status=status.HTTP_404_NOT_FOUND)

        friend_requests = FriendShipRequest.objects.filter(
            (Q(sender=user) & Q(receiver=friend)) | (Q(sender=friend) & Q(receiver=user)),
            status=FriendShipRequest.ACCEPTED
        )
        if friend_requests.exists():
            friend_requests.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No friend found.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(operation_description='Отменить отправленный запрос на дружбу', tags=['Друзья'])
    def cancel_friend_request(self, request, pk=None):
        user = request.user
        friend_id = request.data.get('friend_id')
        friend = self._get_friend(friend_id)
        if friend is None:
            return Response({'error': 'Friend not found.'}, status=status.HTTP_404_NOT_FOUND)

        friend_request = FriendShipRequest.objects.filter(sender=user, receiver=friend,
                                                          status=FriendShipRequest.REQUESTED).first()
        if friend_request:
            friend_request.delete()
            return Response({'success': 'Friend request canceled.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No pending friend request found.'}, status=status.HTTP_400_BAD_REQUEST)
