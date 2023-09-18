from base.base_tests.tests import BaseViewTestCase
from common.models import Country


class CustomerRegistrationViewTest(BaseViewTestCase):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls):
        cls.url = "/api/v1/customer/registration/"
        Country.objects.create(id=1, name=cls.faker.country())
        cls.valid_data = cls.get_reg_data(country=1)
        cls.invalid_data = cls.get_reg_data(country='1', birthday='19992, 02, 34')

    @classmethod
    def get_reg_data(cls, **kwargs):
        data = {
            "password": cls.faker.word(),
            "username": cls.faker.word(),
            "first_name": cls.faker.first_name(),
            "last_name": cls.faker.last_name(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "birthday": cls.faker.date_object(),
        }
        data.update(kwargs)
        return data

    def setUp(self):
        super().setUp()

    def test_01_create_user(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 201)

        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 400)
