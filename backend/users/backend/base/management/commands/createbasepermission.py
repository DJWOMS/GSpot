import sys

from django.core.management.base import BaseCommand

from base.models import BasePermission


class BasePermissionCreatingCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("args", metavar="--name")
        parser.add_argument("args", metavar="--codename")

    def handle(self, *args, **options):
        model = self.get_permission_model()
        name = sys.argv[-2]
        codename = sys.argv[-1]
        if not model.objects.filter(codename=codename):
            print("Permission is creating")
            model.objects.create(
                name=name,
                codename=codename,
            )
        else:
            print("Permission already created!")

    @staticmethod
    def get_permission_model() -> BasePermission:
        raise NotImplementedError
