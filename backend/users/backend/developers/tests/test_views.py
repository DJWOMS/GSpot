from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from admins.models import Admin
from developers.models import Company, CompanyUser

User = get_user_model()

class CompanyViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создаем пользователей
        self.superuser = Admin.objects.create(username='superuser', password='password123', email='admin@123.ru')
        self.staffuser = CompanyUser.objects.create(username='staffuser', password='password123', is_staff=True, email='staff@123.ru')
        self.regularuser = CompanyUser.objects.create(username='regularuser', password='password123', email='user@123.ru')
        self.companyuser1 = CompanyUser.objects.create(username='companyuser1', password='password123', email='user1@123.ru')
        self.companyuser2 = CompanyUser.objects.create(username='companyuser2', password='password123', email='user2@123.ru')
        self.companyuser3 = CompanyUser.objects.create(username='companyuser3', password='password123123213', email='user1232@123.ru')

        # Создаем компании и добавляем пользователей
        self.company1 = Company.objects.create(title='Test Company 1', description='Test description', created_by=self.staffuser, email='comp12@123.ru')
        self.company1.all_user_this_company.add(self.companyuser1, self.companyuser2)
        self.company2 = Company.objects.create(title='Test Company 2', description='Test description', created_by=self.companyuser2, email='comp2@123.ru')
        self.company2.all_user_this_company.add(self.companyuser1,self.companyuser2)
        self.company3 = Company.objects.create(title='Test Company 3', description='Test description', created_by=self.regularuser, email='comp32@123.ru')
        self.company3.all_user_this_company.add(self.companyuser1)

        self.list_url = reverse('company-list')
        self.detail_url = reverse('company-detail', args=[self.company1.id])

    def test_list_companies_as_superuser(self):
        """Список компаний для superuser должен возвращать все компании."""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_companies_as_staffuser(self):
        """Список компаний для staffuser должен возвращать только компании, которые он создал."""
        self.client.force_authenticate(self.staffuser)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_companies_as_company_user(self):
        """Список компаний для companyuser1 должен возвращать только те, где он является участником."""
        self.client.force_authenticate(self.companyuser1)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_companies(self):
        """Получение списка всех компаний"""
        self.client.force_authenticate(self.staffuser)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_company(self):
        """Получение детальной информации о компании"""
        self.client.force_authenticate(self.staffuser)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Company 1')
        self.assertEqual(response.data['created_by'], self.staffuser.id)

    def test_create_company(self):
        """Создание новой компании"""
        self.client.force_authenticate(self.companyuser3)
        data = {
            'title': 'New Company123123',
            'description': 'New description',
            'email': 'new_company123123@example.com',
            'created_by': self.companyuser3.pk
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_company(self):
        """Обновление информации о компании"""
        self.client.force_authenticate(self.staffuser)
        data = {'title': 'Updated Company', 'description': 'Updated description'}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Company')
        self.assertEqual(response.data['description'], 'Updated description')

    def test_delete_company(self):
        """Удаление компании"""
        self.client.force_authenticate(self.staffuser)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Company.objects.filter(id=self.company1.id).exists())
