from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser




class CustomUserAdmin(DefaultUserAdmin):
    model = CustomUser
    fieldsets = (
        DefaultUserAdmin.fieldsets + (
            (None, {'fields': ('date_of_birth', 'profile_photo')})
        )

    )
    add_fieldsets = (
        DefaultUserAdmin.add_fieldsets + (None, {'fields':('date_of_birth')})
    )



class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'publication_year')
    list_filter = ("publication_year",)
    search_fields = ("author",)

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)