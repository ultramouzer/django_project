from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'blog.views.hello', name='hello'),
    url(r'^hello/(?P<yourname>\w+)/$', 'blog.views.hello_name', name='hello_name'),
    url(r'^edmundisagod/$', 'blog.views.imsleepy', name = 'imsleepy'),
    url(r'^time/$', 'blog.views.time', name = 'time'),
    url(r'^no/$', 'blog.views.no', name = 'no'),
    url(r'^review/$', 'blog.views.all_reviews', name = 'all_reviews'),
    url(r'^review/new/$', 'blog.views.new_review', name='new_review'),
    url(r'^review/random/$', 'blog.views.random', name='random'),
]