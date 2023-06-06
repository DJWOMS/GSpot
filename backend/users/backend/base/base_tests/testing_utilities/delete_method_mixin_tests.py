from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class DeleteMethodTestingMixin:
    """Mixin for testing the create method"""

    client: APIClient

    @classmethod
    def test_delete_204(cls, pk, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.delete(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @classmethod
    def test_delete_403(cls, pk, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.delete(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @classmethod
    def test_delete_404(cls, pk, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.delete(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
