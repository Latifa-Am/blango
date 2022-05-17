from django.shortcuts import render
from django.utils import timezone
from blog.models import Comment, Post

# Creating views
def index(request):
    comments = Comment.objects.filter()
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts,"comments":comments})