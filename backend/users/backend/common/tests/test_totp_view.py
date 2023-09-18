from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.totp import TOTPToken
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.urls import reverse


class TestCheckTOTPToken(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.check_totp_url = reverse("check-totp")
        cls.set_password_url = reverse("totp-set-password")
        cls.totp = TOTPToken()
        cls.developer = cls.create_user(CompanyUser)
        cls.administrator = cls.create_user(Admin)
        cls.customer = cls.create_user(CustomerUser)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser]) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        user = model.objects.create_user(**data)
        return user

    def test_totp_for_developer(self):
        test_token = self.totp.generate_totp()
        self.totp.add_to_redis(test_token, self.developer)

        data = {"totp_token": test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({"password": self.faker.word()})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)

    def test_totp_for_admin(self):
        test_token = self.totp.generate_totp()
        self.totp.add_to_redis(test_token, self.administrator)

        data = {"totp_token": test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({"password": self.faker.word()})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)

    def test_totp_for_customer(self):
        test_token = self.totp.generate_totp()
        self.totp.add_to_redis(test_token, self.customer)

        data = {"totp_token": test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({"password": self.faker.word()})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)
