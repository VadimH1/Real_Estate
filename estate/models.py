from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=2000)

    def __str__(self):
        return self.username


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    pub_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.header
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    text = models.TextField(max_length=2000)
    pub_date = models.DateField('date published')  
    announcement = models.ForeignKey(Announcement, verbose_name='published', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.name}, {self.announcement}"


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

