# Generated by Django 4.1.7 on 2023-04-14 10:46

import base.model_fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSchedulerPrice',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('amount', base.model_fields.AmountField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('currency', models.CharField(choices=[('RUB', 'Rub'), ('USD', 'Usd'), ('KZT', 'Kzt'), ('EUR', 'Eur')], default='RUB', max_length=3, verbose_name='Currency')),
                ('created_by', models.UUIDField(verbose_name='Created by')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created at')),
                ('from_dttm', models.DateTimeField(verbose_name='From dttm')),
                ('to_dttm', models.DateTimeField(verbose_name='To dttm')),
                ('is_active', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('price', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='finance.price')),
            ],
            options={
                'verbose_name': 'historical scheduler price',
                'verbose_name_plural': 'historical scheduler prices',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSale',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('from_dttm', models.DateTimeField(verbose_name='From dttm')),
                ('to_dttm', models.DateTimeField(verbose_name='To dttm')),
                ('discount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount')),
                ('is_active', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('offer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='finance.offer')),
            ],
            options={
                'verbose_name': 'historical sale',
                'verbose_name_plural': 'historical sales',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('amount', base.model_fields.AmountField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('currency', models.CharField(choices=[('RUB', 'Rub'), ('USD', 'Usd'), ('KZT', 'Kzt'), ('EUR', 'Eur')], default='RUB', max_length=3, verbose_name='Currency')),
                ('created_by', models.UUIDField(verbose_name='Created by')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created at')),
                ('updated_by', models.UUIDField(verbose_name='Updated by')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated at')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical price',
                'verbose_name_plural': 'historical prices',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOffer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_by', models.UUIDField(db_index=True, verbose_name='UUID creator')),
                ('is_active', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('price', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='finance.price')),
            ],
            options={
                'verbose_name': 'historical offer',
                'verbose_name_plural': 'historical offers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
