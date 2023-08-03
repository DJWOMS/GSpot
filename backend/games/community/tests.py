import uuid
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Review, Product, Language, GradeChoices


class ReviewCreateAPIViewTestCase(TestCase):
    fixtures = [
        'fixtures/product.json',
        'fixtures/language.json',
    ]

    def setUp(self):
        self.client = APIClient()

        self.valid_payload = {
            'user_uuid': str(uuid.uuid4()),
            'game': str(Product.objects.first().id),
            'text': 'This is a test review.',
            'grade': GradeChoices.LIKE,
            'view_type': True,
            'can_reply': True,
            'language': Language.objects.first().id,
        }
        self.invalid_payload = {
            'user_uuid': str(uuid.uuid4()),
            'text': '',
            'grade': 'InvalidGrade',
            'view_type': True,
            'can_reply': True,
            'language': Language.objects.first().id,
        }

    def test_create_valid_review(self):
        response = self.client.post(
            reverse('add-review'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.get()
        self.assertEqual(review.text, self.valid_payload['text'])
        self.assertEqual(review.grade, self.valid_payload['grade'])
        self.assertEqual(review.language.id, self.valid_payload['language'])

    def test_create_invalid_review(self):
        response = self.client.post(
            reverse('add-review'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Review.objects.count(), 0)

    def test_get_request(self):
        response = self.client.get(
            reverse('add-review'), data=self.valid_payload)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Review.objects.count(), 0)

    def test_delete_request(self):
        response = self.client.delete(
            reverse('add-review'), data=self.valid_payload)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Review.objects.count(), 0)
