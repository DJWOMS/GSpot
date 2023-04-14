from django.core.management.base import BaseCommand
from reference.models import Language, ProductLanguage
from django.core.management import call_command
from core.models import Product
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Language.objects.filter(name__contains='test').exists():
            Language.objects.bulk_create([
                Language(name='English_test'),
                Language(name='Spanish_test'),
                Language(name='French_test'),
            ])
            self.stdout.write('Successfully created test data for Language')

        if not Product.objects.exists():
            call_command('fill_products', 3)

        language = Language.objects.all()
        products = Product.objects.all()
        choice = (False, True)

        if not ProductLanguage.objects.exists():
            for product in products:
                ProductLanguage.objects.create(
                    language=random.choice(language),
                    product=product,
                    interface=random.choice(choice),
                    subtitles=random.choice(choice),
                    voice=random.choice(choice)
                )

        self.stdout.write('Successfully created test data for ProductLanguage')
