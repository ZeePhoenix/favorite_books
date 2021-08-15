# Generated by Django 3.2.6 on 2021-08-15 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_uploaded', to='books_app.user'),
        ),
        migrations.AlterField(
            model_name='book',
            name='users_who_like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_books', to='books_app.user'),
        ),
    ]
