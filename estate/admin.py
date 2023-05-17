from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Announcement, Comment

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Announcement)
admin.site.register(Comment)