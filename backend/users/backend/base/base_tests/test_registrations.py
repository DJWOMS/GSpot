from base.base_tests.tests import TestDataSet
from common.models import Country


class RegistrationUsersDatasetTest(TestDataSet):
    valid_data = [
        {
            "password": "123",
            "username": "Ilya",
            "first_name": "Koverin",
            "last_name": "",
            "email": "gravity@gmail.com",
            "phone": "9805551712",
            "birthday": "1992-09-09",
            "country": 1,
        },
    ]
    invalid_data = [
        {
            "password": "123",
            "username": "Il",
            "first_name": "Kov",
            "last_name": "",
            "email": "gravity123@gmail.com",
            "phone": "9805551712",
            "birthday": "19942-09-09",
            "country": "1",
        },
    ]

    @classmethod
    def perform_create(cls):
        Country.objects.create(id=1, name="Russia")
