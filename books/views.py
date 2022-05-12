from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from books.serializers import *
from books.forms import AddBookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics , viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import *
from .utils import *
###################################################################################################
#####################################   REST API ##################################################

class BookViewSet(viewsets.ModelViewSet):
    # queryset = Books.objects.all()
    serializer_class = BookSerializer 

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Books.objects.all()[:2]
        
        return Books.objects.filter(pk= pk)

    @action(methods=['get'],detail = True)
    def genre(self,request , pk):
        genr = Genre.objects.get(pk = pk)
        return Response({'id':genr.id,'genre': genr.name})

    @action(methods=['get'],detail = False)
    def genres(self,request):
        genres = Genre.objects.all()
        return Response({'genres': GenresSerializer(genres,many=True).data})

    @action(methods=['get'],detail = True)
    def author(self,request , pk):
        author = Authors.objects.get(pk = pk)
        return Response({'id':author.id,'genre': author.name})

    @action(methods=['get'],detail = False)
    def authors(self,request):
        authors = Authors.objects.all()
        return Response({'authors': AuthorsSerializer(authors,many=True).data})







############### INDEX ##################
class HomeBooks(DataMixin,ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    # extra_context = {'title':"Index Main "}

    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Index Page")
        # context['title'] = "Index Page"
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Books.objects.filter(is_published = True)



############### BOOK ##################
class Book(DataMixin ,DetailView):
    model = Books
    template_name = "books/book.html"
    slug_url_kwarg = "book_slug"
    context_object_name = "book"

    def get_queryset(self):
        return Books.objects.filter(slug=self.kwargs['book_slug'] ,is_published = True)

    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['book'])
        # context['title'] = context['book']
        return dict(list(context.items())+list(c_def.items()))





############### PROFILE ##################
@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    
    return render(request, 'books/profile.html', context = context)



############### BOOKMARKS ##################
@login_required
def bookmarks(request):
    context = {
        'title': 'Bookmarks'
    }
    
    return render(request, 'books/bookmarks.html', context = context)



############### BAG ##################

@login_required
def bag(request):
    context = {
        'title': 'Bag'
    }
    
    return render(request, 'books/bag.html', context = context)



############### SEARCH ##################
def search(request):
    if request.POST:
        seacrh_title = request.POST.get('seacrh')

        books = Books.objects.filter(title__contains = seacrh_title) 
    
        context = {
            'books':books,
            'title': 'Search'
        }

        return render(request, 'books/search.html', context = context)
    
    context = {
        'title': 'Search'
    }

    return render(request, 'books/search.html', context = context)




############### PAGE NOT FOUND ##################
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')




    

############### GENRES ##################
def genres(request):
    genre = Genre.objects.all()
    context = {
        'catalog':genre,
        'title': 'Genres'
    }
    return render(request, 'books/catalog.html',context=context)


############### AUTHORS ##################
def authors(request):
    authors = Authors.objects.all()
    context = {
        'catalog':authors,
        'title': 'Authors'
    }
    return render(request, 'books/catalog.html',context=context)

############### LIST OF BOOKS AUTHORS ##################
class BooksOfAuthors(DataMixin, ListView):
    model = Books
    template_name = "books/ListOfBooks.html"
    context_object_name = "books"
    allow_empty = False

    def get_context_data(self, * , object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'List Of Books')
        # context['title'] = "List Of Books"
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Books.objects.filter(author__slug=self.kwargs['author_slug'] ,is_published = True)


############### LIST OF GENRES BOOKS ##################
class BooksOfGenres(DataMixin, ListView):
    model = Books
    template_name = "books/listOfBooks.html"
    context_object_name = "books"
    allow_empty = False

    def get_context_data(self, * , object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'List Of Books')
        # context['title'] = "List Of Books"
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Books.objects.filter(genr__slug=self.kwargs['genre_slug'] ,is_published = True)

    




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
class AddBook(LoginRequiredMixin ,DataMixin ,CreateView):
    form_class = AddBookForm
    template_name = 'books/addbook.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')   

    def get_context_data(self, * , object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = "Add Book"
        c_def = self.get_user_context(title = "Add Book")
        return dict(list(context.items())+list(c_def.items()))