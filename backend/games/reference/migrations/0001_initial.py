# Generated by Django 4.1.7 on 2023-04-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='SubGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgenres', to='reference.genre')),
            ],
            options={
                'db_table': 'sub_genre',
            },
        ),
        migrations.CreateModel(
            name='SubgenreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='reference.genre')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.product')),
                ('subgenre', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subgenre', to='reference.subgenre')),
            ],
            options={
                'db_table': 'sub_genre_product',
            },
        ),
        migrations.AddField(
            model_name='subgenre',
            name='products',
            field=models.ManyToManyField(related_name='subgenre', through='reference.SubgenreProduct', to='core.product'),
        ),
        migrations.CreateModel(
            name='ProductLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.BooleanField(default=True)),
                ('subtitles', models.BooleanField(default=True)),
                ('voice', models.BooleanField(default=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='reference.language')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='langs', to='core.product')),
            ],
            options={
                'db_table': 'product_language',
            },
        ),
        migrations.AddField(
            model_name='genre',
            name='products',
            field=models.ManyToManyField(related_name='genres', through='reference.SubgenreProduct', to='core.product'),
        ),
        migrations.AddConstraint(
            model_name='subgenreproduct',
            constraint=models.UniqueConstraint(fields=('product', 'subgenre', 'genre'), name='unique_genre_game'),
        ),
        migrations.AddConstraint(
            model_name='subgenre',
            constraint=models.UniqueConstraint(fields=('name', 'genre'), name='unique_genre_subgenre'),
        ),
        migrations.AddConstraint(
            model_name='productlanguage',
            constraint=models.UniqueConstraint(fields=('language', 'product'), name='unique_language_game'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_genre'),
        ),
    ]
