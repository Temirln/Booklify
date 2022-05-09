from django.urls import path


from .views import *

urlpatterns =[
    path('',index, name='home'),
    path('login/',login,name='login'),
    path('register/',register,name ='register'),


    path('main/',main,name = 'main'),
    path('authors/',authors,name = 'authors'),
    path('genres/',genres,name = 'genres'),
    path('genres/<slug:category_slug>/',BooksOfGenres ,name = 'BooksOfGenres'),
    # path('listOfBooks/',listOfBooks,name = 'listOfBooks'),

    path('add-book/',addbook ,name = 'addbook'),
    path('search/',search ,name = 'search'),
    path('bag/',bag ,name = 'bag'),
    path('profile/',profile ,name = 'profile'),
    path('bookmarks/',bookmarks ,name = 'bookmarks'),

    # path('book/',book ,name = 'book'),
    path('book/<slug:book_slug>/',book ,name = 'book'),
]