from django.core.management.base import BaseCommand
from community.models import Social


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Fill in test data in social model'''
        test_social_type = ('test_social_type1', 'test_social_type2', 'test_social_type3')
        test_url = ('https://test//url1', 'https://test//url2', 'https://test//url3')
        for index, type in enumerate(test_social_type):
            if Social.objects.filter(type=type).exists():
                print(f'There are have social with type {type} in database')
            else:
                Social.objects.create(type=type, url=test_url[index])
