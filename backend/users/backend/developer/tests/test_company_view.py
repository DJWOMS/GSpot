from typing import Union

from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from customer.models import CustomerUser
from developer.models import Company, CompanyUser
from django.urls import reverse
from rest_framework import status


class CompanyTestAPI(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("company")
        cls.admin_user = cls.create_user(Admin)
        cls.customer_user = cls.create_user(CustomerUser)
        cls.superuser_developer = cls.create_user(CompanyUser, is_superuser=True)
        cls.developer = cls.create_user(CompanyUser)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser], **kwargs) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        if model == Admin:
            return model.objects.create_superuser(**data)
        return model.objects.create_user(**data, **kwargs)

    ##################################
    ####    Testing get method    ####
    ##################################

    def test_get_company_by_user_who_have_his_own_company(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_company_by_user_who_dont_have_any_own_company(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_users_permission_deny(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )
        incorrect_users_list: list[Union[CustomerUser, Admin, CustomerUser]] = [
            self.admin_user,
            self.customer_user,
            self.developer,
        ]
        for user in incorrect_users_list:
            self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(user))
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ##################################
    ###    Testing post method     ###
    ##################################

    def test_superuser_developer_can_create_company(self):
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_superuser_developer_can_create_company_but_invalid_data(self):
        data = {
            "title": str("a" * 51),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_superuser_developer_cant_create_company(self):
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.developer))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_admin_cant_create_company(self):
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin_user))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_customer_user_cant_create_company(self):
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.customer_user))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_unautorized_user_can_create_company(self):
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_superuser_developer_cant_create_multiply_companies(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )
        data = {
            "title": self.faker.word(),
            "description": self.faker.text(),
            "email": self.faker.email(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ##################################
    ###     Testing put method     ###
    ##################################

    def test_developer_can_update_own_company(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )

        new_data = {
            "title": self.faker.word(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.put(self.url, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_developer_can_update_own_company_but_invalid_data(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )

        new_data = {
            "title": str("a" * 51),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.put(self.url, new_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ##################################
    ###   Testing delete method    ###
    ##################################

    def test_developer_can_delete_own_company(self):
        Company.objects.create(
            created_by=self.superuser_developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )

        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.superuser_developer))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_admin_cant_delete_company(self):
        Company.objects.create(
            created_by=self.developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )

        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin_user))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cant_delete_company(self):
        Company.objects.create(
            created_by=self.developer,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
        )

        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.customer_user))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
