from django.db import models


class AdminQuerySet(models.QuerySet):
    def count_admins(self):
        return self.filter(is_superuser=True)


class AdminManager(models.Manager):
    def get_query_set(self):
        return AdminQuerySet(self.model, using=self._db)

    def count_admins(self):
        return self.get_query_set().count_admins()



