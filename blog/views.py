from django.shortcuts import render

# Create your views here.
def home(request, username):
    context = {
        'currentuser':username
    }
    return render(request, 'pages/home.html', context)
