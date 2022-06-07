from re import A
from django.contrib import admin
from books.models import *
from django.utils.safestring import mark_safe

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','time_create','time_update','get_html_photo','content','is_published','genr_id','author_id')
    list_display_links = ('title',)
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('time_create','is_published')
    prepopulated_fields = {'slug':("title",)}
    fields= ('title','slug','genr','author','content','get_html_photo','photo','markbook','is_published','time_create','time_update')
    readonly_fields = ('time_create','time_update','get_html_photo','markbook')

    def get_html_photo(self,object):
        if object.photo:    
            return mark_safe(f"<a href='{object.photo.url}' target='_blank'><img src ='{object.photo.url}' width = 50></a>")
        
    get_html_photo.short_description = "Book Covers Miniature"


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

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','get_html_photo')
    list_display_links = ('id','user')
    search_fields = ('user',)
    fields = ('user','get_html_photo','profile_image')
    readonly_fields = ('get_html_photo',)
    # prepopulated_fields = {'slug':("name",)}

    def get_html_photo(self,object):
        if object.profile_image:    
            return mark_safe(f"<a href='{object.profile_image.url}' target='_blank'><img src ='{object.profile_image.url}' width = 70></a>")
        

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Books , BookAdmin )
admin.site.register(Genre , GenreAdmin)
admin.site.register(Authors , AuthorsAdmin)