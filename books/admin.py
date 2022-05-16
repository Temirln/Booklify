from django.contrib import admin
from books.models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','time_create','time_update','photo','content','is_published','genr_id','author_id')
    list_display_links = ('title',)
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('time_create','is_published')
    prepopulated_fields = {'slug':("title",)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':("name",)}

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':("name",)}


admin.site.register(Books , BookAdmin )
admin.site.register(Genre , GenreAdmin)
admin.site.register(Authors , AuthorsAdmin)