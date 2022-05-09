from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from books.forms import AddBookForm


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
def book(request,book_slug):
    book = Books.objects.get(slug = book_slug)
    context = {
        'book':book,
        'title': 'Book'
    }
    
    return render(request, 'books/book.html', context = context)
    # return HttpResponse(f'<h1>Book ID : {book.title}</h1>')



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




############### GENRES ##################
def genres(request):
    category = Category.objects.all()
    context = {
        'catalog':category,
        'title': 'Genres'
    }
    return render(request, 'books/catalog.html',context=context)


############### AUTHORS ##################
def authors(request):
    # authors = Category.objects.all()
    # context = {
    #     'catalog':authors,
    #     'title': 'Authors'
    # }
    # return render(request, 'books/catalog.html',context=context)
    return HttpResponseNotFound('<h1>Page In Progress</h1>')


############### LIST OF BOOKS ##################
def BooksOfGenres(request,category_slug):
    category = Category.objects.get(slug = category_slug)

    books = Books.objects.filter(cat=category.pk,is_published= True)

    if len(books)==0:
        raise Http404
        
    context = {
        'books': books,
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


############### ADD BOOK ##################
def addbook(request):
    
    if request.method == 'POST':
        form = AddBookForm(request.POST , request.FILES)
        if form.is_valid():            
            form.save()
            return redirect('home')

    else:
        form = AddBookForm()    

    context = {
        'form':form,
        'title': 'addbook'
    }
    return render(request, 'books/addbook.html',context=context)