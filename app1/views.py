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

