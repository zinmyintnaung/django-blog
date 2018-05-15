from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/(?P<username>[-\w]+)/$', blog_views.home, name='username'),
    url(r'^post/(?P<single>[-\w]+)/$', blog_views.single, name='single')
]

