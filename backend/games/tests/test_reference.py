from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from reference.models import Genre
from reference.serializers import GenreSerializer
from rest_framework.test import APITestCase


class GenreAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.genre1 = Genre.objects.create(name='test1')
        self.genre2 = Genre.objects.create(name='test2')
        self.guest_client = Client()
        self.user = User.objects.create_user(username='HasNoName')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_get_genre_list(self):
        url = reverse('genre-list')
        response = self.client.get(url)
        serializer_data = GenreSerializer([self.genre1, self.genre2], many=True).data
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(serializer_data, response.data)

    def test_get_genre_detail(self):
        url = reverse('genre-detail', kwargs={'name': self.genre1.name})
        response = self.client.get(url)
        serializer_data = GenreSerializer(self.genre1).data
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(serializer_data, response.data)

    def test_create_genre_superuser(self):
        '''Авторизованному пользователю запрешено создавать жанры'''
        url = reverse('genre-list')
        data = {'name': 'New Genre'}
        response = self.authorized_client.post(url, data=data)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)


class GenreSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.genre1 = Genre.objects.create(name='test1')
        self.genre2 = Genre.objects.create(name='test2')

    def test_genre_serializer(self):
        data = GenreSerializer([self.genre1, self.genre2], many=True).data
        expected_data = [
            {
                "id": self.genre1.id,
                "name": "test1"
            },
            {
                "id": self.genre2.id,
                "name": "test2"
            }
        ]
        self.assertEqual(data, expected_data)
