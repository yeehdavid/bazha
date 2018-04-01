from django.conf.urls import url
from . import views
app_name = 'Shoes'
urlpatterns = [
    #url(r'^$', views.news, name='news'),
    url(r'^(\d+)/$', views.detail, name='detail'),
]