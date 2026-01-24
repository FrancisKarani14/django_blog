from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from models import Post, Comment
from django.url import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

# create a post
class create_post(CreateView):
    model = Post
    fields = ['title', 'content', 'author']
    template_name = 'app1/create_post.html'
    success_url =reverse_lazy('/') 

# update post
class update_post(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app1/update_post.html'
    success_url =reverse_lazy('/')

# view all posts
class view_posts(ListView):
    model = Post
    template_name = 'app1/view_posts.html'
    context_object_name = 'posts'
