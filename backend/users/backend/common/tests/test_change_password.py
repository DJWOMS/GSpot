from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from base.models import BaseAbstractUser
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.urls import reverse
from rest_framework import status


class ChangePassTestAPI(BaseTestView):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("user_change_password")
        cls.admin = cls.create_user(Admin, password='AdminPassword')
        cls.customer = cls.create_user(CustomerUser, password='CustomerPassword')
        cls.developer = cls.create_user(CompanyUser, password='DeveloperPassword')

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser], **kwargs) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        return model.objects.create_user(**data, **kwargs)

    def test_01_developer_change_password_correct_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "DeveloperPassword",
            "new_password": "NewDeveloperPassword",
            "confirmation_new_password": "NewDeveloperPassword",
        }
        response = self.client.post(self.url, data=data, format="json")
        user: CompanyUser = CompanyUser.objects.get(username=self.developer.username)
        self.assertTrue(user.check_password("NewDeveloperPassword"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_02_developer_change_password_wrong_old_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "wrongpassword",
            "new_password": "NewDeveloperPassword",
            "confirmation_new_password": "NewDeveloperPassword",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_03_developer_change_password_wrong_confirm_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "DeveloperPassword",
            "new_password": "NewDeveloperPassword",
            "confirmation_new_password": "NewDeveloperPassword_w",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_04_change_password_unauthenticate_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        data = {
            "old_password": "AdminPassword",
            "new_password": "NewAdminPassword",
            "confirmation_new_password": "NewAdminPassword",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_05_customer_user_change_password_correct_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.customer))
        data = {
            "old_password": "CustomerPassword",
            "new_password": "NewCustomerPassword",
            "confirmation_new_password": "NewCustomerPassword",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user: CustomerUser = CustomerUser.objects.get(username=self.customer.username)
        self.assertTrue(user.check_password("NewCustomerPassword"))

    def test_06_admin_user_change_password_correct_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        data = {
            "old_password": "AdminPassword",
            "new_password": "NewAdminPassword",
            "confirmation_new_password": "NewAdminPassword",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user: Admin = Admin.objects.get(username=self.admin.username)
        self.assertTrue(user.check_password("NewAdminPassword"))
