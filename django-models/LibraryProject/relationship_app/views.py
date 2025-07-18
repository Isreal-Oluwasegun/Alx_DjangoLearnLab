from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.views.generic import ListView, DetailView

def all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetails(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'




