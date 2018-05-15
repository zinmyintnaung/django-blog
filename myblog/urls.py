from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', blog_views.home),
    url(r'^post/(?P<single>[-\w]+)/$', blog_views.single, name='single'),
    url(r'^category/(?P<category>[-\w]+)/$', blog_views.single, name='category')
]

