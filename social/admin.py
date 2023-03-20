from django.contrib import admin

# Register your models here.
from .models import Profile, Follow, Message

admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Message)