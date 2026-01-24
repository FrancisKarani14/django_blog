from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, User, Profile, Comment


admin.site.register([Post, Comment, Profile])


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'user_type',
        'is_staff',
    )

    list_filter = (
        'user_type',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )
