from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/$', views.user),
    url(r'^(?P<id>\d+)/edit/$', views.edit),
    url(r'^new/$', views.new),
]