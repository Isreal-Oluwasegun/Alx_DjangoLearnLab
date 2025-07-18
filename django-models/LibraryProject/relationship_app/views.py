from django.shortcuts import render
from relationship_app.models import Book, Author, Library, Librarian

def all_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/library_detail.html', {'books':books})
