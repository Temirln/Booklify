from django.urls import path


from .views import *

urlpatterns =[
    path('',index, name='home'),
    path('login/',login,name='login'),
    path('register/',register,name ='register'),
    path('book/<int:post_id>/',book ,name = 'book'),
    path('bag/',bag ,name = 'bag'),
    path('search/',search ,name = 'search'),
    path('catalog/',catalog,name = 'catalog'),
    path('listOfBooks/',listOfBooks,name = 'listOfBooks'),
    path('main/',main,name = 'main'),
    path('profile/',profile ,name = 'profile'),
    path('bookmarks/',bookmarks ,name = 'bookmarks'),
]