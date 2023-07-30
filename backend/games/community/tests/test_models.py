import uuid

from django.test import TestCase
from rest_framework.test import APIClient

from community.models import Comment, Review, Product, Language, GradeChoices


class CommentModelTestCase(TestCase):

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

    def setUp(self):
        self.client = APIClient()
        self.valid_comment = Comment.objects.create(
            user_uuid=uuid.uuid4(),
            review=self.review,
            text="Test comment text"
        )

    def test_models_have_correct__str__(self):
        self.assertCountEqual(str(self.valid_comment), f"Comment {self.valid_comment.id}")
