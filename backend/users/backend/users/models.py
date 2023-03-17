import uuid

from django.db import models
from common.models import BaseUser


class User(BaseUser):
    class Meta:
        db_table = "simple_user"
