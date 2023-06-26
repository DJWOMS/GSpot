import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from customer.models import CustomerUser
from developer.models import Company, CompanyUser


class CompanyTestAPI(BaseTestView, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("company")
        cls.admin_user = Admin.objects.create_superuser(
            username="adminR",
            email="adminR@test.com",
            phone="891123123",
            password="testpass123R",
            is_active=True,
        )
        cls.customer_user = CustomerUser.objects.create_user(
            username="customer_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
            is_active=True,
        )
        cls.superuser_developer = CompanyUser.objects.create_user(
            username="test super_user",
            email="testuser@example.com",
            phone="1234567890",
            password="testpassword",
            is_active=True,
            is_superuser=True,
        )
        cls.developer = CompanyUser.objects.create_user(
            username="emplayer1",
            email="emplayer1@example.com",
            phone="123451290",
            password="testpassword1",
            is_active=True,
            is_superuser=False,
        )

    ##################################
    ###    Testing post method     ###
    ##################################

    def test_superuser_developer_can_create_company(self):
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(
            HTTP_AUTHORIZATION=self.get_token(self.superuser_developer)
        )
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_superuser_developer_can_create_company_but_invalid_data(self):
        data = {
            "title": str("a" * 51),
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(
            HTTP_AUTHORIZATION=self.get_token(self.superuser_developer)
        )
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_superuser_developer_cant_create_company(self):
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_admin_cant_create_company(self):
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin_user))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Company.objects.count(), 0)

    def test_customer_user_cant_create_company(self):
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.customer_user))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_unautorized_user_can_create_company(self):
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Company.objects.count(), 0)

    def test_developer_cant_create_multiply_companies(self):
        company_owner = CompanyUser.objects.create_user(
            username="testuser1",
            email="testuser1@example.com",
            phone="12345617890",
            password="testpassword1",
            is_active=True,
            is_superuser=True,
        )
        Company.objects.create(
            created_by=company_owner,
            title="company",
            description="company_description",
            email="company@email.com",
        )
        data = {
            "title": "My Company",
            "description": "We are a company that does things.",
            "email": "info@mycompany.com",
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ##################################
    ###     Testing put method     ###
    ##################################

    def test_developer_can_update_own_company(self):
        company_owner = self.superuser_developer
        company = Company.objects.create(
            created_by=company_owner,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])
        new_data = {
            "title": "My Company",
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.put(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_developer_cant_update_created_by_field_on_own_company(self):
        company_owner = self.superuser_developer
        company = Company.objects.create(
            created_by=company_owner,
            title="company1",
            description="company_description",
            email="company@email.com",
        )

        url = reverse("company_detail", args=[company.id])
        new_data = {
            "created_by": self.developer,
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.put(url, new_data)
        self.assertEqual(
            company,
            Company.objects.get(
                created_by=CompanyUser.objects.get(id=response.data["created_by"])
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_developer_can_update_own_company_but_invalid_data(self):
        company_owner = self.developer
        company = Company.objects.create(
            created_by=company_owner,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])
        new_data = {
            "title": str("a" * 51),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.put(url, new_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_developer_cant_update_not_own_company(self):
        company_owner = CompanyUser.objects.create_user(
            username="testuser2",
            email="testuser2@example.com",
            phone="12345267890",
            password="testpassword2",
            is_active=True,
        )

        company = Company.objects.create(
            created_by=self.developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )

        url = reverse("company_detail", args=[company.id])

        new_data = {
            "title": "My Company",
        }

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.put(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_user_cant_update_company(self):
        company = Company.objects.create(
            created_by=self.developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )

        url = reverse("company_detail", args=[company.id])

        new_data = {
            "title": "My Company",
        }

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.customer_user))
        response = self.client.put(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_user_cant_update_company(self):
        company = Company.objects.create(
            created_by=self.developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )

        url = reverse("company_detail", args=[company.id])

        new_data = {
            "title": "My Company",
        }

        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.put(url, new_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ##################################
    ###   Testing delete method    ###
    ##################################

    def test_developer_can_delete_own_company(self):
        company_owner = self.superuser_developer
        company = Company.objects.create(
            created_by=company_owner,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(company_owner))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_developer_cant_delete_not_own_company(self):
        not_company_owner = CompanyUser.objects.create_user(
            "company_owner2",
            "company_owner2@mail.ru",
            "980348988",
            "company_owner2",
        )
        company = Company.objects.create(
            created_by=self.superuser_developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(not_company_owner))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_cant_delete_company(self):
        company = Company.objects.create(
            created_by=self.developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin_user))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cant_delete_company(self):
        company = Company.objects.create(
            created_by=self.developer,
            title="company1",
            description="company_description",
            email="company@email.com",
        )
        url = reverse("company_detail", args=[company.id])

        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.customer_user))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
