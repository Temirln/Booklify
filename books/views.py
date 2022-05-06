from calendar import c
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
# from django.shortcuts import render

# Create your views here.

from .models import *


############### INDEX ##################
def index(request):
    books = Books.objects.all() 
    context = {
        'books': books,
        'title': 'Booklify'
    }
    return render(request, 'books/index.html', context = context)



############### BOOK ##################
def book(request,post_id):
    context = {
        'title': 'Book'
    }
    
    return render(request, 'books/book.html', context = context)



############### PROFILE ##################
def profile(request):
    context = {
        'title': 'Profile'
    }
    
    return render(request, 'books/profile.html', context = context)



############### SEARCH RESULT ##################
def searchResult(request):
    context = {
        'title': 'Search Result'
    }
    
    return render(request, 'books/searchResult.html', context = context)




############### BOOKMARKS ##################
def bookmarks(request):
    context = {
        'title': 'Bookmarks'
    }
    
    return render(request, 'books/bookmarks.html', context = context)



############### BAG ##################
def bag(request):
    context = {
        'title': 'Bag'
    }
    
    return render(request, 'books/bag.html', context = context)



############### SEARCH ##################
def search(request):
    context = {
        'title': 'Search'
    }
    
    return render(request, 'books/search.html', context = context)




############### PAGE NOT FOUND ##################
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')




############### CATALOG ##################
def catalog(request):
    context = {
        'title': 'Catalog'
    }
    return render(request, 'books/catalog.html',context=context)


############### LIST OF BOOKS ##################
def listOfBooks(request):
    context = {
        'title': 'List Of Books'
    }
    return render(request, 'books/listOfBooks.html',context=context)



############### MAIN ##################
def main(request):
    context = {
        'title': 'main'
    }
    return render(request, 'books/main.html',context=context)



############### LOGIN ##################
def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'books/login.html',context=context)


############### REGISTER ##################
def register(request):
    context = {
        'title': 'Registration'
    }
    return render(request, 'books/register.html',context=context)