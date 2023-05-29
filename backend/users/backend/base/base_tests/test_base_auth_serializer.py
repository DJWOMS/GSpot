from django.test import TestCase
from rest_framework.exceptions import ValidationError
from administrator.models import Admin

from base.serializers import BaseAuthSerializer


class BaseAuthSerializerTestCase(TestCase):
    def setUp(self):
        self.admin_user = Admin.objects.create_superuser(
            "admin", "admin@example.com", "adminpassword", "9998887766", is_active=True
        )

    def test_valid_credentials(self):
        data = {"email": "admin@example.com", "password": "adminpassword"}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.validated_data["user"], self.admin_user)

    def test_invalid_email(self):
        data = {"email": "invalid@example.com", "password": "adminpassword"}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Email or Password not valid")

    def test_invalid_password(self):
        data = {"email": "admin@example.com", "password": "wrongpassword"}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)

        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Email or Password not valid")

    def test_inactive_user(self):
        self.admin_user.is_active = False
        self.admin_user.save()
        data = {"email": "admin@example.com", "password": "adminpassword"}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "Inactive user")

    def test_banned_user(self):
        self.admin_user.is_banned = True
        self.admin_user.save()
        data = {"email": "admin@example.com", "password": "adminpassword"}
        serializer = BaseAuthSerializer(data=data)
        serializer.Meta.model = Admin
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        error_detail = cm.exception.detail["non_field_errors"][0]
        self.assertEqual(error_detail, "User is banned")
