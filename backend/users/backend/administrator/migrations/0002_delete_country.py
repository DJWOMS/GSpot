# Generated by Django 4.2 on 2023-04-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customeruser_country'),
        ('developer', '0002_alter_companyuser_country'),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]
