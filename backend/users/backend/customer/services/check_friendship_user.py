from customer.models import FriendShipRequest
from django.core.exceptions import ValidationError
from django.db.models import Q


class RequestFriends:
    @staticmethod
    def check_send_request(request_user, user_add):
        if FriendShipRequest.objects.filter(
            Q(sender=request_user, receiver=user_add) | Q(sender=user_add, receiver=request_user),
        ).exists():
            raise ValidationError(message="A friend request has already been sent to this user")

    @staticmethod
    def check_accept_request(request_user, user_add):
        if not FriendShipRequest.objects.filter(
            sender=user_add,
            receiver=request_user,
            status__in=["REQUESTED"],
        ).exists():
            raise ValidationError(message="This user did not send the request")

        elif FriendShipRequest.objects.filter(
            sender=user_add,
            receiver=request_user,
            status__in=["REJECTED"],
        ).exists():
            raise ValidationError(message="The user rejected your request earlier")

        elif FriendShipRequest.objects.filter(
            sender=user_add,
            receiver=request_user,
            status__in=["ACCEPTED"],
        ).exists():
            raise ValidationError(message="You are already friends")

    @staticmethod
    def check_delete_friend(request_user, user_add):
        if not FriendShipRequest.objects.filter(
            Q(sender=user_add, receiver=request_user, status__in=["ACCEPTED"])
            | Q(sender=request_user, receiver=user_add, status__in=["ACCEPTED"]),
        ).exists():
            raise ValidationError(message="This user is not in friends")
