from django.test import TestCase
from developers.serializers import CompanySerializer, CompanyUserSerializer, CompanyEmployeeSerializer

from developers.models import Company, CompanyUser
from developers.serializers import CompanySerializer


class CompanySerializerTest(TestCase):
    def setUp(self):
        self.user = CompanyUser.objects.create(
            username='test_user',
            password='test_password',
            email='test_email@example.com',
        )
        self.user2 = CompanyUser.objects.create(
            username='test_user2',
            password='test_password2',
            email='test_email2@example.com',
        )
        self.company = Company.objects.create(
            created_by=self.user2,
            title='Test Company',
            description='Test Company description',
            email='test_company@example.com',
            is_confirmed=True,
            is_active=True,
        )
        self.serializer_data = {
            'created_by': self.user.pk,
            'title': 'New Test Company',
            'description': 'New Test Company description',
            'email': 'new_test_company@example.com',
            'is_confirmed': False,
            'is_active': True,
        }

    def test_create_valid_company(self):
        serializer = CompanySerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Company.objects.count(), 2)

    def test_update_company(self):
        serializer = CompanySerializer(instance=self.company, data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        updated_company = Company.objects.get(pk=self.company.pk)
        self.assertEqual(updated_company.title, 'New Test Company')
        self.assertEqual(updated_company.description, 'New Test Company description')


class CompanyUserSerializerTest(TestCase):
    def setUp(self):
        self.user = CompanyUser.objects.create(
            username='test_user',
            password='test_password',
            email='test_email@example.com',
        )
        self.serializer_data = {
            'username': 'new_test_user',
            'password': 'new_test_password',
            'email': 'new_test_email@example.com',
            'phone': '1234567890',
            'is_banned': True,
            'is_active': False,
            'is_superuser': True,
            'is_staff': True,
        }

    def test_create_valid_user(self):
        serializer = CompanyUserSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(CompanyUser.objects.count(), 2)

    def test_update_user(self):
        serializer = CompanyUserSerializer(instance=self.user, data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        updated_user = CompanyUser.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.username, 'new_test_user')
        self.assertEqual(updated_user.password, 'new_test_password')


class CompanyEmployeeSerializerTest(TestCase):
    def setUp(self):
        self.user = CompanyUser.objects.create(
            username='test_user',
            password='test_password',
            email='test_email@example.com',
        )
        self.company = Company.objects.create(
            created_by=self.user,
            title='Test Company',
            description='Test Company description',
            email='test_company@example.com',
            poster='test_poster.png',
            is_confirmed=False,
            is_active=True,
        )
        self.serializer_data = {
            'email': 'test_company@example.com',
            'description': 'Test Company description',
            'poster': 'test_poster.png',
            'created_by': self.user.pk,
        }

    def test_serialize_employee(self):
        serializer = CompanyEmployeeSerializer(instance=self.company)
        # self.assertEqual(serializer.data, self.serializer_data)
        self.assertEqual(set(serializer.data.keys()), set(self.serializer_data.keys()))

