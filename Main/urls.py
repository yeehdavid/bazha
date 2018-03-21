from django.conf.urls import url
from . import views

app_name = 'Main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nike/', views.nike, name='nike'),
    url(r'^adidas/', views.adidas, name='index'),
    url(r'^nb/', views.nb, name='index'),
    url(r'^asics/', views.asics, name='index'),
    url(r'^others/', views.others, name='index'),
    # url(r'^new/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
