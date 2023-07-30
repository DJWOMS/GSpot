import uuid
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from community.models import Comment, Review, Product, Language, GradeChoices


class CommentUrlTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.language = Language.objects.create(
            name="test language"
        )
        cls.product = Product.objects.create(
            name='test product',
            developers_uuid=uuid.uuid4(),
            publishers_uuid=uuid.uuid4()

        )
        cls.review = Review.objects.create(
            text="Test rewiew text",
            game_id=cls.product.id,
            grade=GradeChoices.LIKE,
            language=cls.language
        )
        cls.PUBLIC_URLS = {
            reverse("review-comments", kwargs={"review_id": f"{cls.review.id}"}): HTTPStatus.OK
        }

    def setUp(self):
        self.client = APIClient()
        self.valid_comment = Comment.objects.create(
            user_uuid=uuid.uuid4(),
            review=self.review,
            text="Test comment text"
        )

    def test_urls_exists_at_desired_location(self):
        for adress, status in self.PUBLIC_URLS.items():
            with self.subTest(adress=adress):
                response = self.client.get(adress)
                self.assertEqual(response.status_code, status)
