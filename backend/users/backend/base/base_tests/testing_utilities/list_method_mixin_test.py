from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ListMethodTestingMixin:
    """Mixin for testing the list method"""

    client: APIClient

    @classmethod
    def test_list_200_OK(cls, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.get(f"{test.url}")
        test.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def test_list_no_access_permission_code_403(cls, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=user)
        response = cls.client.get(f"{test.url}")
        test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
