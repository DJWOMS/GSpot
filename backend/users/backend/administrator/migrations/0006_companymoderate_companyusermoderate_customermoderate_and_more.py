# Generated by Django 4.2.2 on 2023-06-20 05:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0004_alter_customeruser_managers"),
        ("developer", "0006_company_is_banned"),
        ("administrator", "0005_alter_admin_managers_blockreason"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyModerate",
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
                    "reason",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="block reason",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="block time")),
                (
                    "action",
                    models.CharField(choices=[("B", "Block"), ("U", "Unblock")], max_length=1),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moderate_reasons",
                        to="developer.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Company moderate reason",
                "verbose_name_plural": "Company moderate reasons",
                "db_table": "company_moderate_reasons",
            },
        ),
        migrations.CreateModel(
            name="CompanyUserModerate",
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
                    "reason",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="block reason",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="block time")),
                (
                    "action",
                    models.CharField(choices=[("B", "Block"), ("U", "Unblock")], max_length=1),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "company_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moderate_reasons",
                        to="developer.companyuser",
                    ),
                ),
            ],
            options={
                "verbose_name": "Developer moderate reason",
                "verbose_name_plural": "Developers moderate reasons",
                "db_table": "developer_moderate_reasons",
            },
        ),
        migrations.CreateModel(
            name="CustomerModerate",
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
                    "reason",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="block reason",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="block time")),
                (
                    "action",
                    models.CharField(choices=[("B", "Block"), ("U", "Unblock")], max_length=1),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moderate_reasons",
                        to="customer.customeruser",
                    ),
                ),
            ],
            options={
                "verbose_name": "Customer moderate reason",
                "verbose_name_plural": "Customers moderate reasons",
                "db_table": "customer_moderate_reasons",
            },
        ),
        migrations.DeleteModel(
            name="BlockReason",
        ),
    ]
