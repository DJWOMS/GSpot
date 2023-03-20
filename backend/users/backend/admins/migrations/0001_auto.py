import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.contenttypes.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service_name",
                    models.CharField(max_length=16, verbose_name="Service Name"),
                ),
                ("app_label", models.CharField(max_length=100)),
                (
                    "model",
                    models.CharField(max_length=100, verbose_name="python model class name"),
                ),
            ],
            options={
                "verbose_name": "admin content type",
                "verbose_name_plural": "admin content types",
                "db_table": "admin_content_type",
                "abstract": False,
                "unique_together": {("service_name", "app_label", "model")},
            },
            managers=[
                ("objects", django.contrib.contenttypes.models.ContentTypeManager()),
            ],
        ),
        migrations.CreateModel(
            name="AdminPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("codename", models.CharField(max_length=100, verbose_name="codename")),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admins.admincontenttype",
                        verbose_name="content type",
                    ),
                ),
            ],
            options={
                "verbose_name": "admin permission",
                "verbose_name_plural": "admin permissions",
                "db_table": "admin_permission",
                "ordering": [
                    "content_type__app_label",
                    "content_type__model",
                    "codename",
                ],
                "abstract": False,
                "unique_together": {("content_type", "codename")},
            },
            managers=[
                ("objects", django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name="AdminGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=150, unique=True, verbose_name="name"),
                ),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_query_name="group",
                        to="admins.adminpermission",
                        verbose_name="permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "admin group",
                "verbose_name_plural": "admin groups",
                "db_table": "admin_group",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="last name"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="admins.admingroup",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="admins.adminpermission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "admin",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
