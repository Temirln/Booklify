from django.urls import path


from .views import *

urlpatterns =[
    path('',index, name='home'),
    path('login/',login,name='login'),
    path('register/',register,name ='register'),
    path('book/<int:bookid>/',book ,name = 'book'),
]