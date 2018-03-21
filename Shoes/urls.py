from django.conf.urls import url
from . import views
app_name = 'Shoes'
urlpatterns = [
    #url(r'^$', views.news, name='news'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]