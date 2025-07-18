from django.shortcuts import render
from relationship_app.models import Book, Author, Library, Librarian

def all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})
