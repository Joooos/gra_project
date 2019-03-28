from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'index'),
    # re_path(r'^login/$', views.login, name = 'login'),
    # re_path(r'account/(?P<id>\d+)/profile/$', views.profile, name = 'profile'),
    # re_path(r'account/(?P<id>\d+)/profile/update/$', views.profile_update, name = 'profile_update'),
    # re_path(r'account/(?P<id>\d+)/pwdchange/$', views.pwd_change, name = 'pwd_change'),
    # re_path(r'^logout/$', views.logout, name = 'logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^blank/', views.blank, name='blank'),
    url(r'^profile/', views.profile, name='profile'),
]

