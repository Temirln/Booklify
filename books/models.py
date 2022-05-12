from statistics import mode
from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255,verbose_name="Book Name")
    slug = models.SlugField(max_length=255,unique=True,db_index=True , verbose_name="URL")
    content = models.TextField(blank=True , verbose_name="Content")
    photo = models.ImageField(upload_to = "booklify/book_covers/%d-%m-%Y",verbose_name="Books Covers")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time Updated") 
    is_published = models.BooleanField(default=True, verbose_name="Published?")
    genr = models.ForeignKey('Genre',on_delete=models.PROTECT, null=True, verbose_name="Genre ID", related_name="get_genres_books")
    author = models.ForeignKey('Authors',on_delete=models.PROTECT, null=True, verbose_name="Author ID", related_name="get_authors_books")


    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('book',kwargs={'book_slug':self.slug})

    class Meta:
        verbose_name = "Book"
        verbose_name_plural="Books"
        ordering = ['time_create','title']


class Genre(models.Model):
    name = models.CharField(max_length=100,db_index=True , verbose_name="Genre Name")
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('BooksOfGenres',kwargs={'genre_slug':self.slug})

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural="Genres"
        ordering = ['name']



class Authors(models.Model):
    name = models.CharField(max_length=100,db_index=True , verbose_name="Authors Name")
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('BooksOfAuthors',kwargs={'author_slug':self.slug})

    class Meta:
        verbose_name = "Author"
        verbose_name_plural="Authors"
        ordering = ['name']