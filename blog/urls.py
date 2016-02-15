from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'blog.views.hello', name='hello'),
    url(r'^hello/(?P<yourname>\w+)/$', 'blog.views.hello_name', name='hello_name'),
]
