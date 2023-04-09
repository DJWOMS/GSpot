# Generated by Django 4.1.7 on 2023-04-09 13:17

import apps.base.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payment_accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="user_uid",
            new_name="user_uuid",
        ),
        migrations.AlterField(
            model_name="account",
            name="balance",
            field=apps.base.fields.MoneyField(
                decimal_places=2,
                default=0,
                max_digits=11,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Insufficient Funds"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="balancechange",
            name="amount",
            field=apps.base.fields.MoneyField(
                decimal_places=2,
                default=0,
                editable=False,
                max_digits=11,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Should be positive value"
                    )
                ],
            ),
        ),
    ]
