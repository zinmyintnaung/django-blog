from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def home(request):
    postList = Post.objects.all()
    paginator = Paginator(postList, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'pages/home.html', {'posts':posts})

def single(request, single):
    post = Post.objects.get(id=single)
    context = {
        'post': post
    }
    return render(request, 'pages/single.html', context)
