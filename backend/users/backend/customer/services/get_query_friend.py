from customer.models import FriendShipRequest


def get_queryset_for_delete_user(user):
    requests_friend1 = FriendShipRequest.objects.filter(
        receiver_id=user.id,
        status="ACCEPTED",
    ).values_list("sender", flat=True)

    requests_friend2 = FriendShipRequest.objects.filter(
        sender_id=user.id,
        status="ACCEPTED",
    ).values_list("receiver", flat=True)

    if requests_friend1 and requests_friend2:
        return requests_friend1 | requests_friend2

    elif not requests_friend1:
        return requests_friend2

    return requests_friend1
