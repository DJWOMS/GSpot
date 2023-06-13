from datetime import date
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from customer.models import CustomerUser, FriendShipRequest


class TestFriends:
    def setUp(self):
        self.user1 = CustomerUser.objects.create_user(
            'user1',
            'user@email.com',
            '9808887795',
            'user',
            birthday=date.today(),
            is_active=True,
        )
        self.user2 = CustomerUser.objects.create_user(
            'user2',
            'user1@emai.com',
            '9808887796',
            'user1',
            is_active=True,
            birthday=date.today(),
        )
        self.user3 = CustomerUser.objects.create_user(
            'user3',
            'user_friend@emai.com',
            '9808887797',
            'user_friend',
            is_active=True,
            birthday=date.today(),
        )
        self.user4 = CustomerUser.objects.create_user(
            'user4',
            'user_friend_sender@emai.com',
            '9808887798',
            'user_friend',
            is_active=True,
            birthday=date.today(),
        )
        self.friend1 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status='REQUESTED',
        )
        self.friend1.save()
        self.friend2 = FriendShipRequest(
            sender=self.user3,
            receiver=self.user1,
            status='ACCEPTED',
        )
        self.friend2.save()
        self.friend3 = FriendShipRequest(
            sender=self.user3,
            receiver=self.user4,
            status='REJECTED',
        )
        self.friend3.save()
        self.friend4 = FriendShipRequest(
            sender=self.user4,
            receiver=self.user1,
            status='ACCEPTED',
        )
        self.friend4.save()


class TestAddFriends(TestFriends, APITestCase):
    url = reverse('add-friend')

    def test_request_user(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(self.url)
        self.assertEqual(response.data['count'], 2)
        response = self.client.post(self.url, data={'user_id': self.user3.id}, format='json')
        self.assertEqual(self.client.get(self.url).data['count'], 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.user2.friends.all()), 2)

    def test_active_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_banned_user(self):
        self.user2.is_banned = True
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_add_exist_friend(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(self.url, data={'user_id': self.user4.id}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('non_field_errors')[0], 'You are already friends')

    def test_repeat_request_user(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.post(self.url, data={'user_id': self.user1.id}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json().get('non_field_errors')[0],
            'A friend request has already been sent to this user',
        )

    def test_rejected_user_request(self):
        self.client.force_authenticate(user=self.user4)
        response = self.client.post(self.url, data={'user_id': self.user3.id}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json().get('non_field_errors')[0], 'The user rejected your friend request'
        )


class TestAcceptAddFriends(TestFriends, APITestCase):
    url = reverse('accept-add-friend')

    def test_correct_request_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.data['count'], 1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(self.client.get(self.url).data['count'], 0)
        self.assertEqual(post_response.status_code, 200)

    def test_active_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_banned_user(self):
        self.user2.is_banned = True
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_incorrect_request_user(self):
        self.friend1.status = 'REJECTED'
        self.friend1.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            post_response.json().get('non_field_errors')[0], 'This user did not send the request'
        )

    def test_rejected_request_user(self):
        self.friend1.status = 'REQUESTED'
        self.friend1.save()
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status='REJECTED',
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            post_response.json().get('non_field_errors')[0],
            'The user rejected your request earlier',
        )

    def test_already_friend(self):
        self.friend1.status = 'REQUESTED'
        self.friend1.save()
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status='ACCEPTED',
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'You are already friends')


class TestRejectAddFriends(TestFriends, APITestCase):
    url = reverse('reject-add-friend')

    def test_correct_request_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.data['count'], 1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(self.client.get(self.url).data['count'], 0)
        self.assertEqual(post_response.status_code, 200)

    def test_active_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_banned_user(self):
        self.user2.is_banned = True
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_incorrect_request_user(self):
        self.friend1.status = 'REJECTED'
        self.friend1.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            post_response.json().get('non_field_errors')[0], 'This user did not send the request'
        )

    def test_already_friend(self):
        self.friend1.status = 'REQUESTED'
        self.friend1.save()
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status='ACCEPTED',
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user2.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'You are already friends')


class TestDeleteFriends(TestFriends, APITestCase):
    url = reverse('delete-friend')

    def test_correct_request_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.data['count'], 2)
        post_response = self.client.post(self.url, data={'user_id': self.user4.id}, format='json')
        self.assertEqual(self.client.get(self.url).data['count'], 1)
        self.assertEqual(post_response.status_code, 200)

    def test_active_user(self):
        self.user4.is_active = False
        self.user4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user4.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_banned_user(self):
        self.user4.is_banned = True
        self.user4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user4.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get('non_field_errors')[0], 'ValidationError')

    def test_incorrect_request_user(self):
        self.friend4.status = 'REQUESTED'
        self.friend4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(self.url, data={'user_id': self.user4.id}, format='json')
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            post_response.json().get('non_field_errors')[0], 'This user is not in friends'
        )
