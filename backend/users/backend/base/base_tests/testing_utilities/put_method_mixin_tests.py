from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class PutMethodTestingMixin:
    """Mixin for testing the put method"""

    client: APIClient

    @classmethod
    def test_put(cls, pk: int, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.put(f"{test.url}{pk}/", data)
            test.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def test_put_400(cls, pk: int, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.put(f"{test.url}{pk}/", data)
            test.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def test_put_403(cls, pk: int, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.put(f"{test.url}{pk}/", data)
            test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @classmethod
    def test_put_404(cls, pk: int, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.put(f"{test.url}{pk}/")
            test.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
