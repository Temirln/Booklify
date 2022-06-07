from email.policy import default
from PIL import Image
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255,verbose_name="Book Name")
    slug = models.SlugField(max_length=255,unique=True,db_index=True , verbose_name="URL")
    content = models.TextField(blank=True , verbose_name="Content")
    photo = models.ImageField(upload_to = "booklify/book_covers/%d-%m-%Y",verbose_name="Books Covers")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time Updated") 
    is_published = models.BooleanField(default=True, verbose_name="Published?")
    markbook = models.ManyToManyField(User,related_name="Markbook",default=None)
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



def upload_to(instance, filename):
    return 'booklify/profile_pics/%s/%s' % (instance.user.id,filename)


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_image = models.ImageField(default='booklify/profile_pics/default_profile.png',upload_to =upload_to)

    def __str__(self):
        return self.user.username

    # def save(self):
    #     super().save()

    #     img = Image.open(self.profile_image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_image.path)