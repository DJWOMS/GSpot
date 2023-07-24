import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from base.choices import CurrencyChoices, TypeProductChoices

from community.models import Social
from core.models.other import SystemRequirement
from core.models.product import Product
from reference.models.genres import Genre, GenreProduct
from reference.models.langs import Language, ProductLanguage


class ProductTests(APITestCase):
    fixtures = [
        'fixtures/language.json',
        'fixtures/genre.json'
    ]

    def setUp(self):
        self.user = User.objects.create_superuser(username='username', password='password')
        self.client = APIClient()
        self.client.login(username='username', password='password')

        self.data = {
            'name': 'string',
            'developersUuid': uuid.uuid4(),
            'publishersUuid': uuid.uuid4(),
            'description': 'string',
            'about': 'string',
            'type': TypeProductChoices.GAMES,
            'systemRequirements': [
                {
                    'operatingSystem': SystemRequirement.OSChoices.LINUX,
                    'deviceProcessor': 'string',
                    'deviceMemory': 'string',
                    'deviceStorage': 'string',
                    'deviceGraphics': 'string',
                    'typeRequirements': SystemRequirement.TypeRequirementsChoices.MINIMUM
                }
            ],
            'langs': [
                {
                    'languageName': Language.objects.first().name,
                    'interface': True,
                    'subtitles': True,
                    'voice': False
                }
            ],
            'socials': [
                {
                    'type': Social.SocialMediaTypesChoices.YOUTUBE,
                    'url': 'https://www.youtube.com/'
                }
            ],
            'productOffer': {
                'offer': {
                    'price': {
                        'amount': '123',
                        'currency': CurrencyChoices.RUB,
                        'createdBy': uuid.uuid4(),
                        'updatedBy': uuid.uuid4()
                    },
                    'createdBy': uuid.uuid4(),
                    'isActive': True
                },
                'createdBy': uuid.uuid4()
            },
            'genres': [
                Genre.objects.first().name
            ]
        }
        self.url = reverse('games-list')

    def test_create_valid_product(self):
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(ProductLanguage.objects.count(), 1)
        self.assertEqual(Social.objects.count(), 1)
        self.assertEqual(SystemRequirement.objects.count(), 1)
        self.assertEqual(GenreProduct.objects.count(), 1)

    def test_create_invalid_product_without_system_requirements(self):
        self.data.pop('systemRequirements', None)

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(ProductLanguage.objects.count(), 0)
        self.assertEqual(Social.objects.count(), 0)
        self.assertEqual(SystemRequirement.objects.count(), 0)
        self.assertEqual(GenreProduct.objects.count(), 0)

    def test_create_invalid_product_without_langs(self):
        self.data.pop('langs', None)

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(ProductLanguage.objects.count(), 0)
        self.assertEqual(Social.objects.count(), 0)
        self.assertEqual(SystemRequirement.objects.count(), 0)
        self.assertEqual(GenreProduct.objects.count(), 0)

    def test_create_invalid_product_without_offer(self):
        self.data.pop('productOffer', None)

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(ProductLanguage.objects.count(), 0)
        self.assertEqual(Social.objects.count(), 0)
        self.assertEqual(SystemRequirement.objects.count(), 0)
        self.assertEqual(GenreProduct.objects.count(), 0)

    def test_create_invalid_product_without_genres(self):
        self.data.pop('genres', None)

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(ProductLanguage.objects.count(), 0)
        self.assertEqual(Social.objects.count(), 0)
        self.assertEqual(SystemRequirement.objects.count(), 0)
        self.assertEqual(GenreProduct.objects.count(), 0)

    def test_create_invalid_product_with_invalid_genres(self):
        self.data['genres'] = ['abc']

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(ProductLanguage.objects.count(), 0)
        self.assertEqual(Social.objects.count(), 0)
        self.assertEqual(SystemRequirement.objects.count(), 0)
        self.assertEqual(GenreProduct.objects.count(), 0)
