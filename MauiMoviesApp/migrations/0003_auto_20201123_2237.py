# Generated by Django 2.2.4 on 2020-11-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MauiMoviesApp', '0002_moviemanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='releaseDate',
            field=models.IntegerField(),
        ),
    ]