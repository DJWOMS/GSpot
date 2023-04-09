# Generated by Django 4.1.7 on 2023-03-30 19:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('user_uid', models.UUIDField(db_index=True, editable=False, unique=True)),
                (
                    'balance',
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Insufficient Funds',
                            ),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='BalanceChange',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'amount',
                    models.DecimalField(
                        decimal_places=2,
                        editable=False,
                        max_digits=11,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0,
                                message='Should be positive value',
                            ),
                        ],
                    ),
                ),
                ('date_time_creation', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('is_accepted', models.BooleanField(default=False)),
                (
                    'operation_type',
                    models.CharField(
                        choices=[('WD', 'WITHDRAW'), ('DT', 'DEPOSIT')],
                        max_length=20,
                    ),
                ),
                (
                    'account_id',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='balance_changes',
                        to='payment_accounts.account',
                    ),
                ),
            ],
            options={
                'ordering': ['-date_time_creation'],
            },
        ),
    ]
