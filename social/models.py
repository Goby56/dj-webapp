from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    bio = models.TextField(max_length=1000)
    contact = models.TextField(max_length=300)

class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_set")
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_set")
    date_followed = models.DateField()

class Message(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender_set")
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_set")
    time_sent = models.DateTimeField()
    body = models.TextField(max_length=1000)