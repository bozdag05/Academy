# Generated by Django 4.2.5 on 2023-10-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_movie',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
