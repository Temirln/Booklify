from calendar import c
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
# from django.shortcuts import render

# Create your views here.

from .models import *

def index(request):
    books = Books.objects.all() 
    context = {
        'books': books,
        'title': 'Booklify'
    }
    return render(request, 'books/index.html', context = context)

def book(request,bookid):

    
    context = {
        'title': ''
    }
    return render(request, 'books/book.html', context = context)
    # return HttpResponse(f"Book id :{bookid}",context=context)

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'books/login.html',context=context)

def register(request):
    context = {
        'title': 'Registration'
    }
    return render(request, 'books/register.html',context=context)