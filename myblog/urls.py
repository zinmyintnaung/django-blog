from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^username/(?P<username>[-\w]+)/$', blog_views.home, name='username')
]

