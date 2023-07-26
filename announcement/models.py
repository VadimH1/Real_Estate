from django.db import models
from user.models import User

# Create your models here.

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to="pictures/%Y/%m/%d/", null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.header
