from typing import List

from common.services.jwt.token import Token
from django.test import TestCase
from rest_framework.test import APIClient


class TestDataSet:
    valid_data: List[dict]
    invalid_data: List[dict]

    @classmethod
    def perform_create(cls):
        ...


class TestView:
    client = APIClient()
    url: str

    def test_list(self):
        ...

    @classmethod
    def test_create(cls, valid_data: List[dict], invalid_data: List[dict], test: TestCase):
        for data in valid_data:
            response = cls.client.post(cls.url, data)
            test.assertEqual(response.status_code, 201)
        for data in invalid_data:
            response = cls.client.post(cls.url, data)
            test.assertEqual(response.status_code, 400)


class TestBase:
    @classmethod
    def setUpTestData(cls):
        cls.Meta.dataset.perform_create()

    def test_view(self):
        self.Meta.view.test_create(
            self.Meta.dataset.valid_data,
            self.Meta.dataset.invalid_data,
            self,
        )

    class Meta:
        dataset: TestDataSet
        view: TestView


class BaseTestView:
    url: str

    def setUp(self) -> None:
        self.client = APIClient()

    @staticmethod
    def get_token(user) -> str:
        context = {
            "user_id": str(user.id),
            "role": user._meta.app_label,
        }
        return Token().generate_access_token(context)
