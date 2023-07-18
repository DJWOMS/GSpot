import json

from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.notify.notify import Notify
from common.services.totp import TOTPToken
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.conf import settings
from utils.broker.message import FriendAddedMessage
from utils.broker.rabbitmq import RabbitMQ


class TestRabbitMQ(BaseViewTestCase):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.rabbitmq = RabbitMQ()
        cls.admin_user = cls.create_user(Admin)
        cls.customer_user = cls.create_user(CustomerUser)
        cls.customer_user2 = cls.create_user(CustomerUser)
        cls.developer_user = cls.create_user(CompanyUser)

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
        return model.objects.create_user(**data, **kwargs)

    def test_01_send_and_receive_message_add_friend(self):
        message = FriendAddedMessage(user=self.customer_user, sender_user=self.customer_user2)
        Notify().send_notify(message=message)
        with self.rabbitmq:
            method, properties, body = self.rabbitmq._channel.basic_get(
                queue=settings.NOTIFY_ROUTING_KEY,
                auto_ack=True,
            )
            self.assertIsNotNone(body)
            response = json.loads(body)
            self.assertTrue(response['text'])

    def test_02_send_and_receive_admin_activation_message(self):
        TOTPToken().send_totp(user=self.admin_user)
        with self.rabbitmq:
            method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
                queue=settings.EMAIL_ROUTING_KEY,
                auto_ack=True,
            )
            response = json.loads(body)
            self.assertEqual(response['subject'], 'admin_activation')
            self.assertEqual(response['email'], self.admin_user.email)

    def test_03_send_and_receive_develop_activation_message(self):
        TOTPToken().send_totp(user=self.developer_user)
        with self.rabbitmq:
            method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
                queue=settings.EMAIL_ROUTING_KEY,
                auto_ack=True,
            )
            response = json.loads(body)
            self.assertEqual(response['subject'], 'develop_activation')
            self.assertEqual(response['email'], self.developer_user.email)

    def test_04_send_and_receive_customer_activation_message(self):
        TOTPToken().send_totp(user=self.customer_user)
        with self.rabbitmq:
            method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
                queue=settings.EMAIL_ROUTING_KEY,
                auto_ack=True,
            )
            self.rabbitmq._channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            response = json.loads(body)
            self.assertEqual(response['subject'], 'customer_activation')
            self.assertEqual(response['email'], self.customer_user.email)

    def test_05_send_and_receive_multiple_messages_in_order(self):
        TOTPToken().send_totp(user=self.customer_user)
        TOTPToken().send_totp(user=self.developer_user)
        TOTPToken().send_totp(user=self.admin_user)
        response = list()
        with self.rabbitmq:
            for _ in range(3):
                method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
                    queue=settings.EMAIL_ROUTING_KEY,
                    auto_ack=True,
                )
                if body is not None:
                    response.append(json.loads(body)['subject'])
        self.assertListEqual(
            response,
            ['customer_activation', 'develop_activation', 'admin_activation'],
        )
