from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Comment, Post 

# Creating views
def index(request):
    comments = Comment.objects.filter()
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts,"comments":comments})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})