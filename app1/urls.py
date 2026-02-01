from django.urls import path

from . import views 
from .views import (
    CreatePostView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    DeletePostView
    
)


# register urls
urlpatterns = [
    path('', views.home, name='app1-home'),
    path('items/', CreatePostView.as_view(), name='create-post'),
    path('about/', views.about, name='app1-about'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail')
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
]

