from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from customer.models import CustomerUser, FriendShipRequest
from rest_framework.reverse import reverse


class TestFriends(BaseViewTestCase):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls):
        cls.url_get_all_users = reverse('customers-list')
        cls.url_get_all_request_friends = reverse('list-friends-requests')
        cls.url_get_all_friends = reverse('my-friends')
        cls.user1 = cls.create_user(CustomerUser)
        cls.user2 = cls.create_user(CustomerUser)
        cls.user3 = cls.create_user(CustomerUser)
        cls.user4 = cls.create_user(CustomerUser)
        cls.friend1 = FriendShipRequest(
            sender=cls.user2,
            receiver=cls.user1,
            status="REQUESTED",
        )
        cls.friend1.save()
        cls.friend2 = FriendShipRequest(
            sender=cls.user3,
            receiver=cls.user1,
            status="ACCEPTED",
        )
        cls.friend2.save()
        cls.friend3 = FriendShipRequest(
            sender=cls.user3,
            receiver=cls.user4,
            status="REJECTED",
        )
        cls.friend3.save()
        cls.friend4 = FriendShipRequest(
            sender=cls.user4,
            receiver=cls.user1,
            status="ACCEPTED",
        )
        cls.friend4.save()

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser]) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.text(max_nb_chars=50),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "birthday": cls.faker.date_object(),
            "is_active": True,
        }
        return model.objects.create_user(**data)

    def setUp(self):
        super().setUp()


class TestGetUsersList(TestFriends):
    def test_get_correct_user_list(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(self.url_get_all_users)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 2)
        self.friend1.delete()
        response = self.client.get(self.url_get_all_users)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 3)


class TestGetRetrieveUser(TestFriends):
    url = "customers-detail"

    def test_get_correct_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        self.friend1.delete()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.user1.id), response.data["id"])

    def test_get_already_requested_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_already_friend_retrieve_user(self):
        self.client.force_authenticate(user=self.user3)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_reject_retrieve_user(self):
        self.client.force_authenticate(user=self.user3)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user4.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_is_active_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        self.user1.is_active = False
        self.user1.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_is_banned_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        self.user1.is_banned = True
        self.user1.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)


class TestAddFriends(TestFriends):
    url = "customers-add_friend"

    def test_request_user(self):
        self.client.force_authenticate(user=self.user2)
        response_get = self.client.get(self.url_get_all_users)
        self.assertEqual(response_get.data["count"], 2)
        self.assertEqual(len(self.user2.friends.all()), 1)
        response = self.client.post(reverse(self.url, kwargs={"user_id": self.user3.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get(self.url_get_all_users).data["count"], 1)
        self.assertEqual(len(self.user2.friends.all()), 2)

    def test_active_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_banned_user(self):
        self.user2.is_banned = True
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_add_exist_friend(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse(self.url, kwargs={"user_id": self.user3.id}))
        self.assertEqual(response.status_code, 404)

    def test_repeat_request_user(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.post(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_rejected_user_request(self):
        self.client.force_authenticate(user=self.user4)
        response = self.client.post(reverse(self.url, kwargs={"user_id": self.user3.id}))
        self.assertEqual(response.status_code, 404)


class TestGetListAcceptRequestUser(TestFriends):
    def test_correct_get_list_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url_get_all_request_friends)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.friend1.delete()
        response = self.client.get(self.url_get_all_request_friends)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)


class TestRetrieveAcceptRejectAddFriends(TestFriends):
    url = "retrieve-accept-reject-friend"

    def test_get_retrieve_request_adding_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.user2.id))

    def test_accept_correct_request_user(self):
        self.client.force_authenticate(user=self.user1)
        self.assertEqual(self.client.get(self.url_get_all_request_friends).data["count"], 1)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(response.status_code, 200)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(
            self.client.get(reverse(self.url, kwargs={"user_id": self.user2.id})).status_code,
            404,
        )
        self.assertEqual(self.client.get(self.url_get_all_request_friends).data["count"], 0)

    def test_active_user(self):
        self.user2.is_active = False
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_banned_user(self):
        self.user2.is_banned = True
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_incorrect_request_user(self):
        self.friend1.status = "REJECTED"
        self.friend1.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_rejected_request_user(self):
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status="REJECTED",
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            post_response.json().get("non_field_errors")[0],
            "The user rejected your request earlier",
        )

    def test_already_friend(self):
        self.friend1.status = "REQUESTED"
        self.friend1.save()
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status="ACCEPTED",
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.post(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get("non_field_errors")[0], "You are already friends")

    def test_correct_reject_request_user(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url_get_all_request_friends)
        self.assertEqual(response.data["count"], 1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(self.client.get(self.url_get_all_request_friends).data["count"], 0)
        self.assertEqual(post_response.status_code, 200)

    def test_incorrect_reject_request_user(self):
        self.friend1.status = "REJECTED"
        self.friend1.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_reject_already_friend(self):
        self.friend1.status = "REQUESTED"
        self.friend1.save()
        self.friend6 = FriendShipRequest(
            sender=self.user2,
            receiver=self.user1,
            status="ACCEPTED",
        )
        self.friend6.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user2.id}))
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(post_response.json().get("non_field_errors")[0], "You are already friends")


class TestGetListFriends(TestFriends):
    def test_correct_get_list_friends(self):
        self.client.force_authenticate(user=self.user4)
        response = self.client.get(self.url_get_all_friends)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.friend4.delete()
        response = self.client.get(self.url_get_all_friends)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)


class TestRetrieveDestroyFriends(TestFriends):
    url = "retrieve-destroy-friend"

    def test_get_correct_retrieve_user(self):
        self.client.force_authenticate(user=self.user4)
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.user1.id), response.data["id"])

    def test_not_friend_retrieve_user(self):
        self.client.force_authenticate(user=self.user4)
        self.friend4.delete()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_request_on_add_user(self):
        self.client.force_authenticate(user=self.user4)
        self.friend4.status = "REQUESTED"
        self.friend4.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_request_on_reject_user(self):
        self.client.force_authenticate(user=self.user4)
        self.friend4.status = "REJECTED"
        self.friend4.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_is_active_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        self.user1.is_active = False
        self.user1.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_get_is_banned_retrieve_user(self):
        self.client.force_authenticate(user=self.user2)
        self.user1.is_banned = True
        self.user1.save()
        response = self.client.get(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(response.status_code, 404)

    def test_correct_request_user(self):
        self.client.force_authenticate(user=self.user4)
        response = self.client.get(self.url_get_all_friends)
        self.assertEqual(response.data["count"], 1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(self.client.get(self.url_get_all_friends).data["count"], 0)
        self.assertEqual(post_response.status_code, 200)

    def test_active_user(self):
        self.user4.is_active = False
        self.user4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_banned_user(self):
        self.user4.is_banned = True
        self.user4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(post_response.status_code, 404)

    def test_incorrect_request_user(self):
        self.friend4.status = "REQUESTED"
        self.friend4.save()
        self.client.force_authenticate(user=self.user1)
        post_response = self.client.delete(reverse(self.url, kwargs={"user_id": self.user1.id}))
        self.assertEqual(post_response.status_code, 404)
