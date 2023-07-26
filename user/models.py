from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from uuid import uuid4
import uuid


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address', unique=True, max_length=200)
    password = models.CharField(max_length=2000)
    date_create = models.DateTimeField(auto_now=True)
    uuid_number = models.TextField(null=True)                               #  default=uuid.uuid4, null=True
    
    objects = UserManager()

    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = [] 


class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(default='avatar.png', upload_to='profile_avatars')


    



