from django.core.management.base import BaseCommand

from administrator.models import Admin


class Command(BaseCommand):
    def handle(self, *args, **options):
        # if not Admin.objects.filter(username="admin"):
        #     print("Creating admin account...")
        #     Admin.objects.create_superuser(
        #         email="admin@example.com",
        #         username="admin",
        #         first_name="admin",
        #         last_name="admin",
        #         password="admin",
        #     )
        # else:
        print("Admin already initialized")
