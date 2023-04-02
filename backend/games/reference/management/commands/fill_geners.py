from django.core.management.base import BaseCommand
from reference.models import Genre, SubGenre


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''Fill in test data in genre model'''
        test_genre_name = ('test_genre1', 'test_genre2', 'test_genre3')
        test_subgenre_name = ('test_genre1', 'test_subgenre2', 'test_subgenre3')
        for name in test_genre_name:
            if Genre.objects.filter(name=name).exists():
                print(f'There are have genre with name {name} in database')
            else:
                Genre.objects.create(name=name)
        for index, name in enumerate(test_subgenre_name):
            if SubGenre.objects.filter(name=name).exists():
                print(f'There are have subgenre with name {name} in database')
            else:
                SubGenre.objects.create(
                    name=name,
                    genre=Genre.objects.get(name=test_genre_name[index])
                )
