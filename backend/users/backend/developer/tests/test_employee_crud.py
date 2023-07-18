from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.models import Country
from developer.models import Company, CompanyUser
from django.urls import reverse


class DeveloperTestView(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('developer_users_list')
        Country.objects.create(id=1, name=cls.faker.country())
        cls.company_owner = cls.create_user(CompanyUser)
        company = Company.objects.create(
            id=1,
            created_by=cls.company_owner,
            title=cls.faker.word(),
            description=cls.faker.text(),
            email=cls.faker.email(),
            is_confirmed=True,
            is_active=True,
        )
        cls.company_owner.company = company
        cls.company_owner.save()
        cls.developer = cls.create_user(CompanyUser, company=company)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser], **kwargs) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        return model.objects.create_user(**data, **kwargs)

    def test_010_create_employee(self):
        data = {
            "username": self.faker.word(),
            "email": self.faker.email(),
            "phone": self.faker.random_number(digits=10, fix_len=True),
            "country": 1,
            "is_banned": False,
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.company_owner))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)

    def test_020_get_list_by_company_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.company_owner))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_030_check_permission_not_authorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_040_get_developer_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.company_owner))
        response = self.client.get(f"{self.url}{self.developer.id}/")
        self.assertEqual(response.status_code, 200)

    def test_050_partial_update_developer(self):
        data = {
            "first_name": self.faker.word(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.company_owner))
        response = self.client.put(f"{self.url}{self.developer.id}/", data)
        self.assertEqual(response.status_code, 200)

    def test_060_queryset(self):
        test_company_owner = self.create_user(CompanyUser)
        test_company = Company.objects.create(
            id=2,
            created_by=test_company_owner,
            title=self.faker.word(),
            description=self.faker.text(),
            email=self.faker.email(),
            is_confirmed=True,
            is_active=True,
        )
        test_company_owner.company = test_company
        test_company_owner.save()
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(test_company_owner))
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 0)
        response = self.client.get(f"{self.url}{self.developer.id}/")
        self.assertEqual(response.status_code, 404)
