from django.urls import include, path
from rest_framework import routers
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from .views import *

router = routers.DefaultRouter() # SimpleRouter
router.register(r'book',BookViewSet, basename="book")
print(router.urls)


urlpatterns =[

    path('api/v1/', include(router.urls)),


    path('',cache_page(10)(HomeBooks.as_view()), name='home'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',RegisterUser.as_view(),name ='register'),
    path('password_change/',PasswordChangeView.as_view(template_name = "books/password_change_form.html"),name ='password_change'),
    path('password_success/',password_success,name ='password_success'),


    path('reset_password/',auth_views.PasswordResetView.as_view(),name ='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name ='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name ='password_reset_complete'),

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
    path('bookmark/<int:book_id>',markbook,name = 'markbook'),
    path('contact/',ContactFormView.as_view(),name = "contact"),
    path('contact-success/',contact_success,name = "contact_success"),
    
    path('book/<slug:book_slug>/',Book.as_view() ,name = 'book'),
]