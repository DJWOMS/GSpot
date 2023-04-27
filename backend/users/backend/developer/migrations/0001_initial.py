# Generated by Django 4.1.7 on 2023-04-27 14:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Company title')),
                ('description', models.TextField(verbose_name='Company description')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Company email link')),
                ('poster', models.ImageField(blank=True, upload_to='', verbose_name='Company poster')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Company created date')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='DeveloperGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'developer group',
                'verbose_name_plural': 'developer groups',
                'db_table': 'developer_group',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
            ],
            options={
                'verbose_name': 'Developer permission',
                'verbose_name_plural': 'Developer permissions',
                'db_table': 'Developer permission',
                'ordering': ['codename'],
                'abstract': False,
                'unique_together': {('codename',)},
            },
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Department name')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='developer.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Company department',
                'verbose_name_plural': 'Company department',
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(max_length=12, verbose_name='Developer phone-number')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='Developer avatar')),
                ('is_banned', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_user_this_company', to='developer.company', verbose_name='Company')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country', verbose_name='Developer country')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='developer.department', verbose_name='Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='developer_set', related_query_name='developer', to='developer.developergroup', verbose_name='developer_groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this developer.', related_name='developer_permission_set', related_query_name='developer_permission', to='developer.developerpermission', verbose_name='developer permissions')),
            ],
            options={
                'verbose_name': 'Company user',
                'verbose_name_plural': 'Company Users',
                'db_table': 'company_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=150, verbose_name='value contact')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developer.company')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.contacttype', verbose_name='type contact')),
            ],
            options={
                'verbose_name': 'Company contact',
                'verbose_name_plural': 'Company contacts',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.ManyToManyField(blank=True, related_name='contact_set', related_query_name='contact', through='developer.CompanyContact', to='common.contacttype', verbose_name='Company contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='company_owner', to='developer.companyuser', verbose_name='Company owner'),
        ),
    ]
