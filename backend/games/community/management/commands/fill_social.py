from django.core.management.base import BaseCommand
from community.models import Social
from core.models import Product
import random


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of socials to create')

    def handle(self, *args, **options):
        '''Fill in test data in social model'''

        count = options['count']
        social_type = Social.SocialMediaTypesChoices
        products = Product.objects.all()
        zip_iterator = zip(range(count), products)
        social_count = 0

        if not Product.objects.exists():
            print('Product not created, create Product first!')
        else:
            for count, products in zip_iterator:
                if Social.objects.filter(url=f'https://test.com/url_{count}').exists():
                    print(f'Have social with url https://test.com/url_{count} in database')
                else:
                    Social.objects.create(
                        type=random.choices(social_type.choices)[0][1],
                        url=f'https://test.com/url_{count}',
                        product=products)
                    social_count = social_count + 1

            print(f'Successfully created social objects {social_count}')
