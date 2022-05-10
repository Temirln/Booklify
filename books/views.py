from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from books.forms import AddBookForm


# Create your views here.

from .models import *




############### INDEX ##################
class HomeBooks(ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    # extra_context = {'title':"Index Main "}

    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Index Page"
        return context

    def get_queryset(self):
        return Books.objects.filter(is_published = True)



############### BOOK ##################
class Book(DetailView):
    model = Books
    template_name = "books/book.html"
    slug_url_kwarg = "book_slug"
    context_object_name = "book"

    def get_queryset(self):
        return Books.objects.filter(slug=self.kwargs['book_slug'] ,is_published = True)

    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['book']
        return context





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
class BooksOfGenres(ListView):
    model = Books
    template_name = "books/listOfBooks.html"
    context_object_name = "books"
    allow_empty = False

    def get_context_data(self, * , object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "List Of Books"
        return context 

    def get_queryset(self):
        return Books.objects.filter(cat__slug=self.kwargs['category_slug'] ,is_published = True)

    




# def BooksOfGenres(request,category_slug):
#     category = Category.objects.get(slug = category_slug)
#     books = Books.objects.filter(cat=category.pk,is_published= True)
#     if len(books)==0:
#         raise Http404
#     context = {
#         'books': books,
#         'title': 'List Of Books'
#     }
#     return render(request, 'books/listOfBooks.html',context=context)



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
class AddBook(CreateView):
    form_class = AddBookForm
    template_name = 'books/addbook.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, * , object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add Book"
        return context 


# def addbook(request):
#     if request.method == 'POST':
#         form = AddBookForm(request.POST , request.FILES)
#         if form.is_valid():            
#             form.save()
#             return redirect('home')
#     else:
#         form = AddBookForm()    
#     context = {
#         'form':form,
#         'title': 'addbook'
#     }
#     return render(request, 'books/addbook.html',context=context)