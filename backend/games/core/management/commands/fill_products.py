import random
import uuid

from django.core.management.base import BaseCommand
from base.choices import TypeProductChoices

from core.models import Product, GameDlcLink


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to create')

    def handle(self, *args, **options):
        count = options['count']
        ages = [12, 16, 18]
        statuses = ['M', 'P', 'C']

        for i in range(count):
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

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} products'))
