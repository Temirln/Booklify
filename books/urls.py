from django.urls import include, path
from rest_framework import routers

from .views import *


router = routers.DefaultRouter() # SimpleRouter
router.register(r'book',BookViewSet, basename="book")
print(router.urls)


urlpatterns =[

    path('api/v1/', include(router.urls)),


    path('',HomeBooks.as_view(), name='home'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',RegisterUser.as_view(),name ='register'),


    path('main/',main,name = 'main'),
    path('authors/',authors ,name = 'authors'),
    path('authors/<slug:author_slug>/', BooksOfAuthors.as_view() ,name = 'BooksOfAuthors'),

    path('genres/',genres,name = 'genres'),
    path('genres/<slug:genre_slug>/', BooksOfGenres.as_view() ,name = 'BooksOfGenres'),

    path('add-book/',AddBook.as_view() ,name = 'addbook'),
    path('search/',search ,name = 'search'),
    path('bag/',bag ,name = 'bag'),
    path('profile/',profile ,name = 'profile'),
    path('bookmarks/',bookmarks ,name = 'bookmarks'),
    
    path('book/<slug:book_slug>/',Book.as_view() ,name = 'book'),
]