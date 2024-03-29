# Generated by Django 4.1.7 on 2023-04-17 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_gamedlclink_dlc_alter_gamedlclink_game_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSystemRequirement',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('operating_system', models.CharField(choices=[('LINUX', 'Linux'), ('WINDOWS', 'Windows'), ('MACOS', 'MacOS'), ('PS', 'PlayStation'), ('XBOX', 'XBox')], max_length=7, verbose_name='Operation system')),
                ('device_processor', models.CharField(max_length=100, verbose_name='Processor')),
                ('device_memory', models.CharField(max_length=100, verbose_name='Memory')),
                ('device_storage', models.CharField(max_length=100, verbose_name='Storage')),
                ('device_graphics', models.CharField(max_length=100, verbose_name='Graphics')),
                ('type_requirements', models.CharField(choices=[('MINIMUM', 'Minimals'), ('RECOMMEND', 'Recommends')], max_length=9, verbose_name='System requirement')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('game', models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'type': 'GAMES'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.product')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical system requirement',
                'verbose_name_plural': 'historical system requirements',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, db_index=True, editable=False)),
                ('developers_uuid', models.UUIDField(db_index=True)),
                ('publishers_uuid', models.UUIDField(db_index=True)),
                ('description', models.TextField()),
                ('about', models.TextField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('adult', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('MODERATION', 'Moderation'), ('PUBLISH', 'Publish'), ('CLOSE', 'Close')], default='MODERATION', max_length=10, verbose_name='Status product')),
                ('type', models.CharField(choices=[('GAMES', 'Games'), ('DLC', 'Additions')], max_length=5, verbose_name='Type product')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical product',
                'verbose_name_plural': 'historical products',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
