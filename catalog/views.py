from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import Http404
from django.core.urlresolvers import reverse
#from django.template import loader

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #due_date = Book.objects.get('-due_date')
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='Morning')[:5] # Get 5 books containing the title war
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    #template_name = loader.get_template('catalog/book_list.html')

    """
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    """    
    """
    This is the most important line to return the booklist. Return 100 books
    """
    def get_queryset(self):
        return Book.objects.filter()[:100] # This is the most important line to return the booklist

    
    def book_list_view(request,pk):
        try:
             book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
             raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
        return render(
         request,
        'catalog/book_list.html',
        context={'book':book_id,} 
        )
    
class BookDetailView(generic.DetailView):
    model = Book
    
    def book_detail_view(request,pk):
        try:
             book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
             raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
        return render(
         request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
    
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filterotitle__icontains='Morning')[:5] # Get 5 books containing the title war
    template_name = 'authors/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    """
    This is the most important line to return the author list. Return max. 100 authors 
    """  
    def get_queryset(self):
        return Author.objects.filter()[:100] 


    def author_list_view(request,pk):
        try:
             author_id=Book.objects.get(pk=pk)
        except Author.DoesNotExist:
             raise Http404("Author does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
        return render(
         request,
        'catalog/author_list.html',
        context={'author':author_id,} 
        )  
        
    
    
class AuthorDetailView(generic.DetailView):
    model = Author
    
    def author_detail_view(request,pk):
        try:
             author_id=Author.objects.get(pk=pk)
        except Author.DoesNotExist:
             raise Http404("Author does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
        return render(
         request,
        'catalog/author_detail.html',
        context={'author':author_id,}
    )






















    