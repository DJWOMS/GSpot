from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "country"
        verbose_name = _("country")
        verbose_name_plural = _("countries")