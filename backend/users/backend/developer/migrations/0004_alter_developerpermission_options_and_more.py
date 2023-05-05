# Generated by Django 4.1.7 on 2023-05-05 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('developer', '0003_remove_companyuser_last_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developerpermission',
            options={
                'ordering': ['codename'],
                'verbose_name': 'developer permission',
                'verbose_name_plural': 'developer permissions',
            },
        ),
        migrations.AlterField(
            model_name='companycontact',
            name='type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='common.contacttype',
                verbose_name='type contact',
            ),
        ),
        migrations.AlterModelTable(
            name='developerpermission',
            table='developer_permission',
        ),
    ]
