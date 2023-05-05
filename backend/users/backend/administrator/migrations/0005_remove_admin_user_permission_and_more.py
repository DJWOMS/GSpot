# Generated by Django 4.1.7 on 2023-05-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_alter_adminpermission_options_alter_admin_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='user_permission',
        ),
        migrations.AlterField(
            model_name='admin',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                help_text='Specific permissions for this admin.',
                related_name='admin_set',
                related_query_name='admin',
                to='administrator.adminpermission',
                verbose_name='admin permissions',
            ),
        ),
    ]
