from admins.models import Admin
from django.test import TestCase


class AdminQuerySetTests(TestCase):
    def setUp(self):
        self.admin_first = Admin.objects.create(username='test_admin_1',
                                                password='1234567Qwsa',
                                                email='test_email@mail.ru')
        self.admin_second = Admin.objects.create(username='test_admin_2',
                                                 password='zxc1234567Qwsa',
                                                 email='test_email_second@mail.ru')

    def test_count_admins(self):
        admins = Admin.objects.count_admins()
        self.assertEqual(len(admins), 2)
        self.assertEqual(admins[0].email, self.admin_first.email)
        self.assertEqual(admins[1].username, self.admin_second.username)
