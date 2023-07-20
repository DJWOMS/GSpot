import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.choices import TypeProductChoices

from core.models.product import GameDlcLink, Product


class GameDLCTests(APITestCase):
    fixtures = [
        'fixtures/product.json',
    ]

    def setUp(self):
        Product.objects.create(
            name='string',
            release_date='2011-11-18',
            developers_uuid=uuid.uuid4(),
            publishers_uuid=uuid.uuid4(),
            description='string',
            age=6,
            adult='',
            status='PUBLISH',
            type=TypeProductChoices.DLC
        )

        self.data = {
            'game': Product.objects.filter(type=TypeProductChoices.GAMES).first().id,
            'dlc': [Product.objects.filter(type=TypeProductChoices.DLC).first().id]
        }
        self.url = reverse('dlc-link')

    def test_create_valid_pack(self):
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameDlcLink.objects.count(), 1)

    def test_create_invalid_game_pack(self):
        self.data['game'] = uuid.uuid4()

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(GameDlcLink.objects.count(), 0)

    def test_create_invalid_dlc_pack(self):
        self.data['dlc'] = [uuid.uuid4()]

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(GameDlcLink.objects.count(), 0)

    def test_create_invalid_pack_dlc_instead_of_game(self):
        self.data['game'] = Product.objects.filter(type=TypeProductChoices.DLC).first().id

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(GameDlcLink.objects.count(), 0)

    def test_create_invalid_pack_game_instead_of_dlc(self):
        self.data['dlc'] = [Product.objects.filter(type=TypeProductChoices.GAMES).first().id]
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(GameDlcLink.objects.count(), 0)
