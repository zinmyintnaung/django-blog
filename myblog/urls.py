from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'test/', blog_views.home)
]
