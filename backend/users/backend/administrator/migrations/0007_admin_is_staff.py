# Generated by Django 4.2.2 on 2023-06-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('administrator', '0006_companymoderate_companyusermoderate_customermoderate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
