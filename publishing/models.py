from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    snippet = models.TextField("Code Snippet")
    text = models.TextField("Plain Text")
    image = models.ImageField(upload_to="images")

class Post(models.Model):
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100, choices=[(0, "SNIPPET"), (1, "IMAGE")])
    content_id = models.OneToOneField(Content, on_delete=models.PROTECT)
    pub_date = models.DateTimeField()
    votes = models.IntegerField("upvotes - downvotes")
    publisher_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.ForeignKey("self", on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_sent = models.DateTimeField()
    votes = models.IntegerField("upvotes - downvotes")
    text = models.TextField(max_length=1000)