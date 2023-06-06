from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class RetriveMethodTestingMixin:
    """Mixin for testing the retrive/detail method"""

    client: APIClient

    @classmethod
    def test_retrive_200(cls, pk: int, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.get(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def test_retrive_403(cls, pk: int, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=user)
        response = cls.client.get(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @classmethod
    def test_retrive_404(cls, pk: int, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.get(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
