from common import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "country"
        verbose_name = _("country")
        verbose_name_plural = _("countries")


class ContactType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name contact"))
    icon = models.ImageField(verbose_name=_("icon contact"), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact_type'
        verbose_name = _('contact_type')
        verbose_name_plural = _('contact_types')


class MessageNotifyRabbitMQ(models.Model):
    ADD_FRIEND = "ADD_FRIEND"
    STATUS_CHOICES = ((ADD_FRIEND, "add_friend"),)
    text = models.TextField(
        verbose_name=_('message_notify_rabbitmq'),
        validators=[validators.validate_user_in_text],
    )
    action = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.text

    @property
    def get_text(self):
        return f'{self.text}'

    class Meta:
        db_table = 'message_notify_rabbitmq'
        verbose_name = _('message_notify_rabbitmq')
        verbose_name_plural = _('message_notify_rabbitmq')


class MessageEmailRabbitMQ(models.Model):
    ADMIN_ACTIVATION = "ADMIN_ACTIVATION"
    DEVELOP_ACTIVATION = "DEVELOP_ACTIVATION"
    CUSTOMER_ACTIVATION = "CUSTOMER_ACTIVATION"
    STATUS_CHOICES = (
        (ADMIN_ACTIVATION, 'admin_activation'),
        (DEVELOP_ACTIVATION, 'develop_activation'),
        (CUSTOMER_ACTIVATION, 'customer_activation'),
    )
    url = models.CharField(validators=[validators.validate_totp_in_url])
    text = models.TextField(
        verbose_name=_('message_email_rabbitmq'),
        validators=[validators.validate_url_in_text],
    )
    action = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.text

    @property
    def get_text(self):
        return self.text, self.url

    class Meta:
        db_table = 'message_email_rabbitmq'
        verbose_name = _('message_email_rabbitmq')
        verbose_name_plural = _('message_email_rabbitmq')
