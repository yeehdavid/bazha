from django.conf.urls import url
from . import views
app_name = 'News'
urlpatterns = [
    #url(r'^$', views.news, name='news'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]