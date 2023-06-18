from django.db.models import Q
from rest_framework import serializers, status
from customer.models import CustomerUser, FriendShipRequest
from common.permissions.validators import BannedUserValidatorVerify, ActiveUserValidator
from customer.services.check_friendship_user import RequestFriends


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'avatar', 'username')


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        exclude = ('password', 'is_active', 'is_banned', 'update_at')


class BaseFriendSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()

    def validate(self, attrs):
        receiver_user = self.context["request"].user
        sender_user = CustomerUser.objects.get(pk=attrs['user_id'])
        ActiveUserValidator().validate(sender_user)
        BannedUserValidatorVerify().validate(sender_user)
        self.get_request_function()(receiver_user, sender_user)
        attrs['sender_user'] = sender_user
        attrs['receiver_user'] = receiver_user
        return attrs

    @staticmethod
    def get_request_function():
        raise NotImplementedError


class AddFriendSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()

    def validate(self, attrs):
        request_user = self.context["request"].user
        user_add = CustomerUser.objects.get(pk=attrs['user_id'])
        ActiveUserValidator().validate(user_add)
        BannedUserValidatorVerify().validate(user_add)
        RequestFriends.check_send_request(request_user, user_add)
        attrs['user_add'] = user_add
        attrs['request_user'] = request_user
        return attrs

    def save(self, **kwargs):
        instance = FriendShipRequest(
            sender=kwargs['user'],
            receiver=kwargs['user_add'],
            status='REQUESTED',
        )
        instance.save()
        return instance


class AcceptAddFriendSerializer(BaseFriendSerializer):
    def save(self, **kwargs):
        instance = FriendShipRequest.objects.get(
            sender=kwargs.get('sender_user'),
            receiver=kwargs.get('receiver_user'),
            status='REQUESTED',
        )
        instance.status = 'ACCEPTED'
        instance.save()
        return instance

    @staticmethod
    def get_request_function():
        return RequestFriends.check_accept_request


class RejectAddFriendSerializer(BaseFriendSerializer):
    def save(self, **kwargs):
        instance = FriendShipRequest.objects.get(
            sender=kwargs.get('sender_user'),
            receiver=kwargs.get('receiver_user'),
            status='REQUESTED',
        )
        instance.status = 'REJECTED'
        instance.save()
        return instance

    @staticmethod
    def get_request_function():
        return RequestFriends.check_accept_request


class DeleteFriendSerializer(BaseFriendSerializer):
    def save(self, **kwargs):
        instance = FriendShipRequest.objects.filter(
            Q(
                sender=kwargs.get('sender_user'),
                receiver=kwargs.get('receiver_user'),
                status='ACCEPTED',
            )
            | Q(
                sender=kwargs.get('receiver_user'),
                receiver=kwargs.get('sender_user'),
                status='ACCEPTED',
            )
        )[0]
        instance.status = 'REJECTED'
        instance.save()
        return instance

    @staticmethod
    def get_request_function():
        return RequestFriends.check_delete_friend
