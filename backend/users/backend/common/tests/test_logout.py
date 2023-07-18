from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.urls import reverse


class TestJWTLogoutView(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("logout")
        cls.developer = cls.create_user(CompanyUser)
        cls.admin = cls.create_user(Admin)
        cls.customer = cls.create_user(CustomerUser)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser]) -> BaseAbstractUser:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        return model.objects.create_user(**data)

    def create_refresh_token(self, user) -> dict:
        refresh_token = self.get_tokens(user)
        return {"refresh_token": refresh_token.get('refresh')}

    def test_01_logout_developer(self):
        refresh_token = self.create_refresh_token(self.developer)
        response = self.client.post(self.url, refresh_token, format="json")
        self.assertEqual(response.status_code, 205)

    def test_02_logout_admin(self):
        refresh_token = self.create_refresh_token(self.admin)
        response = self.client.post(self.url, refresh_token, format="json")
        self.assertEqual(response.status_code, 205)

    def test_03_logout_customer(self):
        refresh_token = self.create_refresh_token(self.customer)
        response = self.client.post(self.url, refresh_token, format="json")
        self.assertEqual(response.status_code, 205)
