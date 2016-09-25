from django.conf.urls import url
from django.shortcuts import render
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #getting album details
    url(r'^(?P<albums_id>[0-9]+)/$', views.detail, name='detail'),
]
