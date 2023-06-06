from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class CreateMethodTestingMixin:
    """Mixin for testing the create method"""

    client: APIClient

    @classmethod
    def test_create_201(cls, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.post(f"{test.url}", data)
            test.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @classmethod
    def test_create_400(cls, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.post(f"{test.url}", data)
            test.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @classmethod
    def test_create_403(cls, user, data_list, test: TestCase):
        for data in data_list:
            cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
            response = cls.client.post(f"{test.url}", data)
            test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
