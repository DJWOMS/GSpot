from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce


class AdminQuerySet(models.QuerySet):
    def with_workers_count(self):
        return self.annotate(
            workers_count=Coalesce(Count('username'), 0)
        )
