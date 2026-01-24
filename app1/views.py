from django.shortcuts import render
from .models import Post, Comment


# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

# create a post
def create_post(request):
    pass