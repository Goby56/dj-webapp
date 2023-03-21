from django.shortcuts import render

from .models import Post, Content

# Create your views here.
def index(request):
    top_posts = Post.objects.order_by("-votes")
    return render(request, "publishing/index.html", {"top_posts": top_posts, "Content": Content})
