from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin"):
            print("Creating admin account...")
            User.objects.create_superuser(
                email="admin@example.com",
                username="admin",
                first_name="admin",
                last_name="admin",
                password="admin",
            )
        else:
            print("Admin already initialized")
