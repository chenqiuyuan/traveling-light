# -*- encoding:utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "homepage"
urlpatterns = [
    url(r'^$', views.index, name='index',),
    url(r'^your_name/$', views.get_name, name='your_name'),
    url(r'^upload_pic/$', views.upload_pic, name='upload_pic'),
    url(r'^登陆页面.html$', views.to_login, name='login'),
    url(r'^注册页面.html$', views.to_sign_up, name='to_sign_up'),
    url(r'^sign_up/$',views.sign_up,name='sign_up'),
    url(r'^login/$', views.login, name='login')
]
