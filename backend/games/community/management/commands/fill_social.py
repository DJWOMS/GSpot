from django.core.management.base import BaseCommand
from community.models import Social


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, default=3, help='Number of socials to create')

    def handle(self, *args, **options):
        '''Fill in test data in social model'''
        count = options['count']
        for i in range(count):
            if Social.objects.filter(type=f'Test_social_type{i}').exists():
                print(f'There are have social with type "Social_test_{i}" in database')
            else:
                Social.objects.create(type=f'Social_test_{i}', url=f'https://test.com/url{i}')
                print('Object created')
