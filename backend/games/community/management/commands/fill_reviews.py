import uuid
from django.core.management.base import BaseCommand
from community.models import Review
from core.models import Product
from reference.models import Language


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Review.objects.filter(text__contains='test data').exists():
            self.stdout.write(self.style.SUCCESS('Test data already exists for Review model'))
            return
        else:
            # Create test data
            language = Language.objects.get(id=1)
            product1 = Product.objects.get(id='0e3a2e04-6b2c-4821-a7ef-c0f48f671309')
            Review.objects.bulk_create([
                Review(
                    user_uuid=uuid.uuid4(),
                    game=product1,
                    text='Test data review 1',
                    grade='A+',
                    view_type=True,
                    can_reply=True,
                    language=language,
                ),
                Review(
                    user_uuid=uuid.uuid4(),
                    game=product1,
                    text='Test data review 2',
                    grade='B',
                    view_type=True,
                    can_reply=True,
                    language=language,
                ),
                Review(
                    user_uuid=uuid.uuid4(),
                    game=product1,
                    text='Test data review 3',
                    grade='C',
                    view_type=True,
                    can_reply=False,
                    language=language,
                ),
            ])
            self.stdout.write(self.style.SUCCESS('Test data created successfully'))
