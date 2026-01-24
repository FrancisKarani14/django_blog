from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# user model
class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        
    ) 
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='user')
    def __str__(self):
        return self.username
