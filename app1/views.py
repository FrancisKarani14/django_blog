from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from models import Post, Comment
from django.url import reverse_lazy

# Create your views here.
class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'createpost.html'
    success_url = reverse_lazy('post_list')


# get the list of posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


#gets the details of the specific post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'