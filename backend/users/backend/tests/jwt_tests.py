from rest_framework.test import APITestCase
from developers.models import CompanyUser, DeveloperPermission, DeveloperContentType
from service.jwt.create_jwt import get_token_user


class JwtApiTestCase(APITestCase):
    def setUp(self):
        self.first_user = CompanyUser.objects.create(
            username='user_of_company',
            email='email@mail.ru',
            password='usercompany'
        )
        self.first_user.is_active = True
        self.first_user.save()
        self.second_user = CompanyUser.objects.create(
            username='user_of_company_2',
            email='email2@mail.ru',
            password='usercompany2'
        )
        self.second_user.is_active = True
        self.second_user.save()

        self.content_type = DeveloperContentType.objects.create(
            service_name='User',
            app_label='developer',
            model='developeruser',
        )
        self.content_type.save()

        self.developer_permission = DeveloperPermission.objects.create(
            name='add',
            content_type=self.content_type,
            codename='123'
        )
        self.developer_permission.save()
        self.first_user.user_permissions.add(self.developer_permission)

    def test_create_jwt_first_user(self):
        token = get_token_user(self.first_user, 'developer')
        self.assertEqual("<class 'dict'>", str(type(token)))

    def test_create_jwt_second_user(self):
        token = get_token_user(self.second_user, 'developer')
        self.assertEqual("<class 'dict'>", str(type(token)))
