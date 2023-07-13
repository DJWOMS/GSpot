import pika
from base.base_tests.tests import BaseTestView
from common.models import Country
from django.conf import settings
from utils.broker.rabbitmq import RabbitMQ


class DeveloperRegistrationViewTest(BaseTestView):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls):
        cls.url = "/api/v1/developer/registration/"
        Country.objects.create(id=1, name=cls.faker.country())
        cls.valid_data = cls.get_reg_data(country=1)
        cls.invalid_data = cls.get_reg_data(email='aa@mmm')

    @classmethod
    def get_reg_data(cls, **kwargs):
        data = {
            "password": cls.faker.word(),
            "username": cls.faker.word(),
            "first_name": cls.faker.first_name(),
            "last_name": cls.faker.last_name(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "birthday": cls.faker.date_object(),
        }
        data.update(kwargs)
        return data

    def setUp(self):
        super().setUp()

    def tearDown(self) -> None:
        self.rabbitmq = RabbitMQ()
        with self.rabbitmq:
            try:
                self.rabbitmq._channel.queue_purge(queue=settings.EMAIL_ROUTING_KEY)
            except pika.exceptions.ChannelClosedByBroker:
                pass
            try:
                self.rabbitmq._channel.queue_purge(queue=settings.NOTIFY_ROUTING_KEY)
            except pika.exceptions.ChannelClosedByBroker:
                pass

    def test_01_create_user(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 201)

        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 400)
