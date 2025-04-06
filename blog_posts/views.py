from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, "blog_posts/postlist.html", {"posts": posts},)  # Corrected template path
