from django.shortcuts import render
# from .models import Post, Comment
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Post, Comment, User, Profile
from django.urls import reverse_lazy

# Create your views here.
# home view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

# about view
def about(request):
    return render(request, 'about.html', {'title': 'About'})
# creates a post
class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app1/create_post.html'
    success_url = reverse_lazy('post_list')


# get the list of posts
class PostListView(ListView):
    model = Post
    template_name = 'app1/post_list.html'
    context_object_name = 'posts'


#gets the details of the specific post
class PostDetailView(DetailView):
    model = Post
    template_name = 'app1/post_detail.html'
    context_object_name = 'post'

# updates a specific post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app1/post_update.html'
    success_url = reverse_lazy('post_list')

# deletes a specific post
class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    context_object_name = 'post'


