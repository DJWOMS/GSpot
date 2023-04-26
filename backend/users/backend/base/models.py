import uuid

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import PermissionManager, GroupManager, AbstractUser
from django.contrib.contenttypes.models import ContentTypeManager
from django.db import models

from django.apps import apps


class BaseAbstractUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    is_staff = None

    class Meta:
        abstract = True


class BaseContentType(models.Model):
    service_name = models.CharField("Service Name", max_length=16)
    app_label = models.CharField(max_length=100)
    model = models.CharField(_("python model class name"), max_length=100)
    objects = ContentTypeManager()

    class Meta:
        abstract = True
        unique_together = [["service_name", "app_label", "model"]]

    def __str__(self):
        return self.app_labeled_name

    @property
    def name(self):
        model = self.model_class()
        if not model:
            return self.model
        return str(model._meta.verbose_name)

    @property
    def app_labeled_name(self):
        model = self.model_class()
        if not model:
            return self.model
        return "%s | %s" % (model._meta.app_label, model._meta.verbose_name)

    def model_class(self):
        """Return the model class for this type of content."""
        try:
            return apps.get_model(self.app_label, self.model)
        except LookupError:
            return None

    def get_object_for_this_type(self, **kwargs):
        """
        Return an object of this type for the keyword arguments given.
        Basically, this is a proxy around this object_type's get_object() model
        method. The ObjectNotExist exception, if thrown, will not be caught,
        so code that calls this method should catch it.
        """
        return self.model_class()._base_manager.using(self._state.db).get(**kwargs)

    def get_all_objects_for_this_type(self, **kwargs):
        """
        Return all objects of this type for the keyword arguments given.
        """
        return self.model_class()._base_manager.using(self._state.db).filter(**kwargs)

    def natural_key(self):
        return self.app_label, self.model


class BasePermission(models.Model):
    name = models.CharField(_("name"), max_length=255)
    content_type = None  # Must be overridden by child class
    codename = models.CharField(_("codename"), max_length=100)

    objects = PermissionManager()

    class Meta:
        abstract = True
        unique_together = [["codename"]]
        ordering = ["codename"]

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return self.codename


class BaseGroup(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    permissions = None  # Must be overridden in child class

    objects = GroupManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name,