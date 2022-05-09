# Generated by Django 4.0.4 on 2022-05-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Book Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('photo', models.ImageField(upload_to='booklify/book_covers/%d-%m-%Y', verbose_name='Books Covers')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time Updated')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published?')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.category', verbose_name='Category ID')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
