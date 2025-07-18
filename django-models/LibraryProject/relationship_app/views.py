from django.shortcuts import render
from django.views.generic.detail import DetailView
from relationship_app.models import Book
from .models import Library
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    
class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

