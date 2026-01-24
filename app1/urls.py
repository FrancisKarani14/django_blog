from django.urls import path

from . import views

# register urls
urlpatterns = [
    path('', views.home, name='app1-home'),
]

