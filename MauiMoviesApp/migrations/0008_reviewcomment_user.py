# Generated by Django 2.2.4 on 2020-11-30 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MauiMoviesApp', '0007_delete_moviemanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='MauiMoviesApp.User'),
        ),
    ]
