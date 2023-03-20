from common.models import BaseUser
from django.db import models


class Admin(BaseUser):
    class Meta:
        db_table = "admin"


class ContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=50)
    app_label = models.ImageField(upload_to='media/users', blank=True)
    model = models.CharField(max_length=50)

    class Meta:
        db_table = 'content_type'


class Permission(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'permission'


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'group'


class GroupPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    class Meta:
        db_table = 'group_permission'


class UserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    user = models.ForeignKey(Admin, on_delete=models.PROTECT)

    class Meta:
        db_table = 'user_permissions'


class GroupUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(Admin, on_delete=models.PROTECT)

    class Meta:
        db_table = 'group_user_permissions'
