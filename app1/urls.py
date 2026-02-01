from django.urls import path

from . import views 
from .views import (
    CreatePostView,
    PostListView,
    
)


# register urls
urlpatterns = [
    path('', views.home, name='app1-home'),
    path('items/', CreatePostView.as_view(), name='create-post'),
    path('about/', views.about, name='app1-about'),
    path('posts/', PostListView.as_view(), name='post-list')
]

