from django.contrib import admin
from .models import Post, User, Profile, Comment

# Register your models here.

admin.site.register(Post, User, Comment, Profile)

