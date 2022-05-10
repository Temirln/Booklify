from django.urls import path


from .views import *

urlpatterns =[
    path('',HomeBooks.as_view(), name='home'),
    path('login/',login,name='login'),
    path('register/',register,name ='register'),


    path('main/',main,name = 'main'),
    path('authors/',authors,name = 'authors'),

    path('genres/',genres,name = 'genres'),
    path('genres/<slug:category_slug>/', BooksOfGenres.as_view() ,name = 'BooksOfGenres'),

    path('add-book/',AddBook.as_view() ,name = 'addbook'),
    path('search/',search ,name = 'search'),
    path('bag/',bag ,name = 'bag'),
    path('profile/',profile ,name = 'profile'),
    path('bookmarks/',bookmarks ,name = 'bookmarks'),

    path('book/<slug:book_slug>/',Book.as_view() ,name = 'book'),
]