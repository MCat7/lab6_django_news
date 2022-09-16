from django.urls import path, re_path

from . import views

app_name = 'news'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
    re_path(r'^([0-9]+)/return', views.index, name='return'),
  #  re_path(r'^([0-9]+)/text/$', views.text, name='text')

]
