"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import list_books, LibraryDetailView
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name="library_detail"),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('admin-view/', views.admin_view, name='Admin'),
    path('librarian-view/', views.librarian_view, name='Librarian'),
    path('member-view/', views.member_view, name='Member'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),

   



]
