from django.test import TestCase
from developers.models import Company, CompanyUser


class CompanyModelTestCase(TestCase):

    def setUp(self):
        self.owner = CompanyUser.objects.create(username='owner', password='password', email='owner@test.com')
        self.company = Company.objects.create(created_by=self.owner, title='Test Company', description='Test description',
                                               email='test@test.com')

    def test_company_creation(self):
        self.assertTrue(isinstance(self.company, Company))
        self.assertEqual(str(self.company), 'Test Company')
        self.assertEqual(self.company.description, 'Test description')

    def test_company_user_relation(self):
        self.assertEqual(self.company.created_by, self.owner)

    def test_company_user_creation(self):
        user = CompanyUser.objects.create(username='user', password='password', email='user@test.com', company=self.company)
        self.assertTrue(isinstance(user, CompanyUser))
        self.assertEqual(user.company, self.company)
