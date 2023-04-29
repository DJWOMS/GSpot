import argparse
import random
import uuid

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from base.choices import TypeProductChoices

from reference.models.langs import Language, ProductLanguage
from community.models import Review, Comment, Reaction, Social
from reference.models.genres import Genre, SubGenre
from core.models.product import GameDlcLink, Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-all', action='store_true', help='Fill all data')
        parser.add_argument('-r', action='store_true', help='Fill reviews')
        parser.add_argument('-l', action='store_true', help='Fill languages')
        parser.add_argument('-g', action='store_true', help='Fill genres')
        parser.add_argument('-s', action='store_true', help='Fill social')
        parser.add_argument('-cnt', nargs=1, help='Count of records')

    def handle(self, *args, **options):
        if 'cnt' not in options:
            raise CommandError('Count of records must be specified.')
        self.count = int(options['cnt'][0])

        if options['all']:
            self.fill_all_data()
        elif options['r']:
            self.fill_reviews()
        elif options['l']:
            self.fill_languages()
        elif options['g']:
            self.fill_genres()
        elif options['s']:
            self.fill_social()
        else:
            raise CommandError('No valid flag specified.')

    def fill_all_data(self):
        self.fill_genres()
        self.fill_languages()
        self.fill_reviews()

    def fill_reviews(self):
        if not Product.objects.exists():
            self.fill_products()
        if not Language.objects.exists():
            self.fill_languages()
        if Review.objects.filter(text__contains='Test').exists():
            self.stdout.write('Test data for Reviews already exists')
            return

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

    def fill_languages(self):
        if not Language.objects.filter(name__contains='test').exists():
            Language.objects.bulk_create([
                Language(name='English_test'),
                Language(name='Spanish_test'),
                Language(name='French_test'),
            ])
            self.stdout.write('Successfully created test data for Language')

        if not Product.objects.exists():
            self.fill_products()

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

    def fill_genres(self):
        existing_genres = set(Genre.objects.values_list('name', flat=True))
        existing_subgenres = set(SubGenre.objects.values_list('name', flat=True))

        for i in range(self.count):
            genre_name = f'test_genre_{i}'
            subgenre_name = f'test_subgenre_{i}'

            if genre_name not in existing_genres:
                Genre.objects.create(name=genre_name)
            else:
                print(f'There is already a genre with the name {genre_name} in the database')

            if subgenre_name not in existing_subgenres:
                genre = Genre.objects.get(name=genre_name)
                SubGenre.objects.create(name=subgenre_name, genre=genre)
            else:
                print(f'There is already a subgenre with the name {subgenre_name} in the database')

    def fill_products(self):
        ages = [12, 16, 18]
        statuses = ['M', 'P', 'C']

        for i in range(self.count):
            developers_uuids = uuid.uuid4()
            publishers_uuids = uuid.uuid4()
            product = Product.objects.create(
                name=f'Product {i}',
                developers_uuid=developers_uuids,
                publishers_uuid=publishers_uuids,
                description=f'Description {i}',
                about=f'About {i}',
                age=random.choice(ages),
                adult=f'Adult_descriptions {i}',
                status=random.choice(statuses),
                type=TypeProductChoices.GAMES
            )

            for j in range(random.randint(1, 5)):
                dlc = Product.objects.create(
                    name=f'DLC {j}',
                    developers_uuid=developers_uuids,
                    publishers_uuid=publishers_uuids,
                    description=f'Descriptions {i}',
                    about=f'Abouts {i}',
                    age=random.choice(ages),
                    adult=f'Adult_descriptions {i}',
                    status=random.choice(statuses),
                    type=TypeProductChoices.DLC
                )

                GameDlcLink.objects.create(game=product, dlc=dlc)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {self.count} products'))

    def fill_social(self):
        social_type = Social.SocialMediaTypesChoices
        products = Product.objects.all()
        zip_iterator = zip(range(self.count), products)
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
