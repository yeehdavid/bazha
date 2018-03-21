from django.conf.urls import url

from . import views
app_name = 'order'

urlpatterns = [
    url(r'^order/post/(?P<order_pk>[0-9]+)/$', views.post_order, name='post_order'),
]