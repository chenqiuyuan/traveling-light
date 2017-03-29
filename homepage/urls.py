# -*- encoding:utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "homepage"
urlpatterns = [
    url(r'^$', views.index, name='index',),
    url(r'^your_name/$', views.get_name, name='your_name'),
    url(r'^upload_pic/$', views.upload_pic, name='your_name'),
    url(r'^登陆页面.html$', views.login, name='login'),
    url(r'^resources/', views.login, name='login')
    # url(r'^$', views.index, name='index'),
]
