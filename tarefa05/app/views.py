from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    posts = Post.objects.order_by("-data_publicacao")
    return render(
        request,
        "app/index.html",
        {"posts": posts},
    )

def post(request, id):
    postagem = get_object_or_404(Post, id=id)
    return render(
        request,
        "app/post.html",
        {"post": postagem},
    )