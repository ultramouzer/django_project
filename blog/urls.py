from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'blog.views.hello', name='hello'),
    url(r'^aboutme/(?P<yourname>\w+)/$', 'blog.views.aboutme', name='aboutme')
]
