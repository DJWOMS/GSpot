from django.test import TestCase
from django.urls import reverse

from faker import Faker

from base.base_tests.test_crud_contry_and_contentType import BaseViewSetTestCase
from base.base_tests.testing_utilities.utils import MixinTestView
from common.models import Country
from common.tests.factory import CountryFactory


fake = Faker()


class CountryTestsCase(BaseViewSetTestCase, TestCase):
    url: str = reverse("countries-list")
    invalid_data = [{"name": ""}, {"name": str("a" * 51)}]
    valid_data_for_put = [{"name": "renamed country"}, {"name": "renamed country1"}]
    valid_data_for_create = [
        {"name": fake.country()[:49]},
    ]

    @classmethod
    def setUpClass(cls):
        cls.countries = CountryFactory.create_batch(5)
        super().setUpClass()

    class Meta:
        view: MixinTestView = MixinTestView
        model_for_test: Country = Country
