# Generated by Django 4.0.4 on 2022-05-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_books_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.IntegerField(default=14),
            preserve_default=False,
        ),
    ]
