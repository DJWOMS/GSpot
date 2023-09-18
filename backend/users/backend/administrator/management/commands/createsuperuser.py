from administrator.models import Admin
from django.contrib.auth.management.commands.createsuperuser import (
    Command as SuperUserCommand,
)


class Command(SuperUserCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.UserModel = Admin
        self.username_field = self.UserModel._meta.get_field(self.UserModel.USERNAME_FIELD)
