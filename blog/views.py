from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request, username):
    posts = Post.objects.all()

    context = {
        'posts':posts,
        'currentuser':username
    }
    return render(request, 'pages/home.html', context)

def single(request, single):
    post = Post.objects.get(id=single)
    context = {
        'post': post
    }
    return render(request, 'pages/single.html', context)
