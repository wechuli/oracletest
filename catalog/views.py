from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Book, Author, BookInstance, Genre
#This is a function based view
@login_required
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
    num_genres=Genre.objects.count()

     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits,'num_genres':num_genres} # num_visits appended
    )
#We can also implement a class based view
class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book

class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Author
    
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')