# Generated by Django 3.2.6 on 2021-08-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20210815_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_who_like',
        ),
        migrations.AddField(
            model_name='book',
            name='users_who_like',
            field=models.ManyToManyField(null=True, related_name='liked_books', to='books_app.User'),
        ),
    ]
