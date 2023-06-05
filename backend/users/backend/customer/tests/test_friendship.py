from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.utils import json

from customer.models import CustomerUser, FriendShipRequest


class FriendshipViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomerUser.objects.create(username='user1', birthday='1990-10-13', email='user1@mail.com',
                                                 phone='+79994163145')
        self.user2 = CustomerUser.objects.create(username='user2', birthday='2000-11-15', email='user2@mail.com',
                                                 phone='+79994164477')

    def test_add_friend(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/customer/users/{id}/add_friend/'.format(id=self.user1.id)
        json_data = json.dumps({'friend_id': str(self.user2.id)})
        response = self.client.post(url, json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FriendShipRequest.objects.count(), 1)
        self.assertEqual(FriendShipRequest.objects.first().sender, self.user1)
        self.assertEqual(FriendShipRequest.objects.first().receiver, self.user2)

    def test_accept_friend_request(self):
        self.client.force_authenticate(user=self.user1)
        friend_request = FriendShipRequest.objects.create(sender=self.user2, receiver=self.user1)
        url = '/api/v1/customer/users/{id}/accept_friend_request/'.format(id=self.user1.id)
        data = {'friend_id': self.user2.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        friend_request.refresh_from_db()
        self.assertEqual(friend_request.status, FriendShipRequest.ACCEPTED)

    def test_reject_friend_request(self):
        self.client.force_authenticate(user=self.user1)
        friend_request = FriendShipRequest.objects.create(sender=self.user2, receiver=self.user1)
        url = '/api/v1/customer/users/{id}/reject_friend_request/'.format(id=self.user1.id)
        data = {'friend_id': self.user2.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        friend_request.refresh_from_db()
        self.assertEqual(friend_request.status, FriendShipRequest.REJECTED)

    def test_remove_friend(self):
        self.client.force_authenticate(user=self.user1)
        FriendShipRequest.objects.create(sender=self.user1, receiver=self.user2,
                                         status=FriendShipRequest.ACCEPTED)
        FriendShipRequest.objects.create(sender=self.user2, receiver=self.user1,
                                         status=FriendShipRequest.ACCEPTED)
        url = '/api/v1/customer/users/{id}/remove_friend/'.format(id=self.user1.id)
        data = {'friend_id': self.user2.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FriendShipRequest.objects.count(), 0)

    def test_add_same_friend_twice(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/customer/users/{id}/add_friend/'.format(id=self.user1.id)
        json_data = json.dumps({'friend_id': str(self.user2.id)})
        response = self.client.post(url, json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FriendShipRequest.objects.count(), 1)

        # Try adding the same friend again
        response = self.client.post(url, json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(FriendShipRequest.objects.count(), 1)

    def test_cancel_friend_request(self):
        self.client.force_authenticate(user=self.user1)
        FriendShipRequest.objects.create(sender=self.user1, receiver=self.user2,
                                         status=FriendShipRequest.REQUESTED)
        url = '/api/v1/customer/users/{id}/cancel_friend_request/'.format(id=self.user1.id)
        data = {'friend_id': self.user2.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FriendShipRequest.objects.count(), 0)

    def test_cancel_friend_request_no_request(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/customer/users/{id}/cancel_friend_request/'.format(id=self.user1.id)
        data = {'friend_id': self.user2.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'No pending friend request found.')
