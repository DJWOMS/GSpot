import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True)

    groups = None
    user_permissions = None

    class Meta:
        abstract = True
