import json
from datetime import date

from administrator.models import Admin
from base.base_tests.teardown_base_test import TearDown
from common.services.notify.notify import Notify
from common.services.totp import TOTPToken
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.conf import settings
from rest_framework.test import APITestCase
from utils.broker.message import FriendAddedMessage
from utils.broker.rabbitmq import RabbitMQ


class TestRabbitMQ(TearDown, APITestCase):
    fixtures = ['fixtures/message_and_notify']

    def setUp(self) -> None:
        self.rabbitmq = RabbitMQ()
        self.admin_user = Admin.objects.create_user(
            username='user1230',
            email='user1230@email.com',
            phone='98088127792',
            password='user',
            is_active=True,
        )
        self.customer_user = CustomerUser.objects.create_user(
            username='user25',
            email='user54@email.com',
            phone='9808887691',
            password='user',
            birthday=date.today(),
            is_active=True,
        )
        self.customer_user2 = CustomerUser.objects.create_user(
            username='user225',
            email='user541@email.com',
            phone='98088876912',
            password='user',
            birthday=date.today(),
            is_active=True,
        )
        self.developer_user = CompanyUser.objects.create_user(
            username='user1234',
            email='email123@mail.ru',
            password='usercompany124',
            phone='89991234561',
            company=None,
        )

    def test_01_send_and_receive_message_add_friend(self):
        Notify().send_notify(
            user=self.customer_user,
            sender_user=self.customer_user2,
            message=FriendAddedMessage,
        )
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
