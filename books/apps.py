from tabnanny import verbose
from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
    verbose_name= "Booklify"

    def ready(self):
        import books.signals
