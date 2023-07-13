from administrator.models import Admin
from base.serializers import BaseAuthSerializer
from django.test import TestCase
from faker import Faker
from rest_framework.exceptions import ValidationError

fake = Faker(locale="ru_RU")


class BaseAuthSerializerTestCase(TestCase):
    def setUp(self):
        self.password = fake.word()
        self.admin_user = Admin.objects.create_superuser(
            username=fake.first_name(),
            password=self.password,
            email=fake.email(),
            phone="9998887766",
            is_active=True,
        )

    def test_010_valid_credentials(self):
        data = {"email": self.admin_user.email, "password": self.password}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.validated_data["user"], self.admin_user)

    def test_011_invalid_email(self):
        data = {"email": fake.email(), "password": self.password}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Email or Password not valid")

    def test_012_invalid_password(self):
        data = {"email": self.admin_user.email, "password": fake.word()}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)

        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Email or Password not valid")

    def test_013_inactive_user(self):
        self.admin_user.is_active = False
        self.admin_user.save()
        data = {"email": self.admin_user.email, "password": self.password}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Inactive user")

    def test_014_banned_user(self):
        self.admin_user.is_banned = True
        self.admin_user.save()
        data = {"email": self.admin_user.email, "password": self.password}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "User is banned")
