from django.contrib import admin

# Register your models here.
from .models import Content, Post, Comment

admin.site.register(Content)
admin.site.register(Post)
admin.site.register(Comment)