from django.contrib import admin
from .models import Post, User, Profile, Comment
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register([Post, Comment, Profile])

@admin.register(User)
class CustomuserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff']
    list_filter = ['user_type', 'is_staff', 'is_superuser', 'is_active']


