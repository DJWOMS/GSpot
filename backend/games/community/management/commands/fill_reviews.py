import uuid
from django.core.management.base import BaseCommand
from community.models import Review, Comment, Reaction
from core.models import Product
from reference.models import Language
import random
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Product.objects.exists():
            call_command('fill_products', 4)
        if not Language.objects.exists():
            call_command('fill_languages')
        if Review.objects.filter(text__contains='Test').exists():
            self.stdout.write('Test data for Reviews already exists')
            return

        # Create test data
        view_type_can_reply = (False, True)
        grade_choice = ('Like', 'Dislike')

        language = Language.objects.all()
        products = Product.objects.all()

        min_quantity = 3
        max_quantity = 4

        for product in products:
            num_reviews = random.randint(min_quantity, max_quantity)

            for i in range(num_reviews):
                review = Review(
                    user_uuid=uuid.uuid4(),
                    game=product,
                    text=f'Test review #{i+1} for {product.name}',
                    grade=random.choice(grade_choice),
                    view_type=random.choice(view_type_can_reply),
                    can_reply=random.choice(view_type_can_reply),
                    language=random.choice(language)
                )
                review.save()
        self.stdout.write('Successfully created test data for Reviews')

        if not Review.objects.exists():
            self.stdout.write('There are no reviews in the database')
            return

        reviews = Review.objects.all()

        for review in reviews:
            num_comment = random.randint(min_quantity, max_quantity)
            num_reaction = random.randint(min_quantity, max_quantity)

            for i in range(num_comment):
                comment = Comment(
                    review=review,
                    text=f'Test comment #{i+1} for review {review.id}'
                )
            comment.save()
            for i in range(num_reaction):
                reaction = Reaction(
                    review=review,
                    like_type=random.choice(grade_choice),
                )
            reaction.save()
        self.stdout.write('Successfully created comments and reactions')
