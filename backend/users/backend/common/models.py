from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "country"
        verbose_name = _("country")
        verbose_name_plural = _("countries")


class ContactType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name contact'))
    icon = models.ImageField(verbose_name=_('icon contact'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
