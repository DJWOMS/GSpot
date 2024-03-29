# Generated by Django 4.1.7 on 2023-04-14 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedlclink',
            name='dlc',
            field=models.ForeignKey(limit_choices_to={'type': 'DLC'}, on_delete=django.db.models.deletion.CASCADE, related_name='game_link', to='core.product'),
        ),
        migrations.AlterField(
            model_name='gamedlclink',
            name='game',
            field=models.ForeignKey(limit_choices_to={'type': 'GAMES'}, on_delete=django.db.models.deletion.CASCADE, related_name='dlc_link', to='core.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('MODERATION', 'Moderation'), ('PUBLISH', 'Publish'), ('CLOSE', 'Close')], default='MODERATION', max_length=10, verbose_name='Status product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('GAMES', 'Games'), ('DLC', 'Additions')], max_length=5, verbose_name='Type product'),
        ),
        migrations.AlterField(
            model_name='systemrequirement',
            name='game',
            field=models.ForeignKey(limit_choices_to={'type': 'GAMES'}, on_delete=django.db.models.deletion.CASCADE, related_name='system_requirements', to='core.product'),
        ),
        migrations.AlterField(
            model_name='systemrequirement',
            name='operating_system',
            field=models.CharField(choices=[('LINUX', 'Linux'), ('WINDOWS', 'Windows'), ('MACOS', 'MacOS'), ('PS', 'PlayStation'), ('XBOX', 'XBox')], max_length=7, verbose_name='Operation system'),
        ),
        migrations.AlterField(
            model_name='systemrequirement',
            name='type_requirements',
            field=models.CharField(choices=[('MINIMUM', 'Minimals'), ('RECOMMEND', 'Recommends')], max_length=9, verbose_name='System requirement'),
        ),
    ]
