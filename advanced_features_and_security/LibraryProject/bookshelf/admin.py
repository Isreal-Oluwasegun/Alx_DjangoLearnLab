from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


content_type = ContentType.objects.get_for_model(Book)

view_permission = Permission.objects.create(
    codename='can_view',
    name='Can view book',
    content_type=content_type,
)
create_permission = Permission.objects.create(
    codename='can_create',
    name='Can create book',
    content_type=content_type,
)

edit_permission = Permission.objects.create(
    codename='can_edit',
    name='Can edit book',
    content_type=content_type,
)

delete_permission = Permission.objects.create(
    codename='can_delete',
    name='Can delete book',
    content_type=content_type,
)
editor_group, created = Group.objects.get_or_create(name='Editors')
if created:
    editor_group.permissions.add(view_permission)
    editor_group.permissions.add(create_permission)

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