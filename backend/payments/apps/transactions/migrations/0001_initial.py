# Generated by Django 4.1.7 on 2023-04-19 16:49

import apps.base.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', apps.base.fields.MoneyField(decimal_places=2, max_digits=11, validators=[django.core.validators.MinValueValidator(0, message='Should be positive value'), django.core.validators.MaxValueValidator(10000, message='Should be not greater than 10000')])),
                ('item_uuid', models.UUIDField(db_index=True, editable=False)),
                ('is_frozen', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_purchase_account_from', to='payment_accounts.account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_purchase_account_to', to='payment_accounts.account')),
                ('developer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='developer_info', to='payment_accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='TransferHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', apps.base.fields.MoneyField(decimal_places=2, editable=False, max_digits=11, validators=[django.core.validators.MinValueValidator(0, message='Should be positive value')])),
                ('date_time_creation', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history_accounts_from', to='payment_accounts.account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history_accounts_to', to='payment_accounts.account')),
            ],
            options={
                'ordering': ['-date_time_creation'],
            },
        ),
        migrations.CreateModel(
            name='ItemPurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_creation', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('operation_type', models.CharField(choices=[('CT', 'CREATED'), ('CD', 'COMPLETED')], max_length=50)),
                ('item_purchase_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='item_purchases_history', to='transactions.itempurchase')),
            ],
            options={
                'ordering': ['-date_time_creation'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item_purchases', models.ManyToManyField(to='transactions.itempurchase')),
            ],
        ),
    ]
