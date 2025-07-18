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

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from bookshelf.views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
import django.contrib.auth.views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    # path('lib', include('relationship_app.urls')),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(template_name="registration/login.html"), name='login'),
    # path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='passowrd_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='reset'),
    # path('reset/confirm/', auth_views.PasswordResetCompleteView.as_view(), name='reset_cofirm'),
    path('' , include('bookshelf.urls')),
    path('', include('relationship_app.urls')),
]
