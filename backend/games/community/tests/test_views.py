import uuid
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from community.models import Comment, Review, Product, Language, GradeChoices


DELTA_POST = 5
TEST_POSTS_RANGE = 20 + DELTA_POST


class CommentViewTestCase(TestCase):

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

    def test_comment_created_with_correct_data(self):
        response = self.client.get(reverse("review-comments",
                                           kwargs={"review_id": f"{self.review.id}"}))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["id"], self.valid_comment.id)
        self.assertEqual(response.json()["results"][0]["text"], self.valid_comment.text)
        self.assertEqual(response.json()["results"][0]["userUuid"],
                         str(self.valid_comment.user_uuid))


class PaginatorViewsTest(TestCase):

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
        self.authorized_client = APIClient()
        comment_list = []
        self.uuid = uuid.uuid4()
        for i in range(TEST_POSTS_RANGE):
            comment_list.append(Comment(
                user_uuid=self.uuid,
                review=self.review,
                text=f"Test comment text №{i}"))
        Comment.objects.bulk_create(comment_list)

    def test_paginator_context(self):
        self.assertEqual(Comment.objects.all().count(), 25)

    def test_correct_page_context_authorized_client(self):
        response_page_1 = self.client.get(reverse("review-comments",
                                          kwargs={"review_id": f"{self.review.id}"}))
        response_page_2 = self.client.get(reverse("review-comments",
                                          kwargs={"review_id": f"{self.review.id}"}) + '?page=2')
        count_comments_page_1 = len(response_page_1.json()["results"])
        count_comments_page_2 = len(response_page_2.json()["results"])
        self.assertEqual(count_comments_page_1, 20)
        self.assertEqual(count_comments_page_2, TEST_POSTS_RANGE - 20)
