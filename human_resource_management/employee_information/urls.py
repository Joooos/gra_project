from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    url(r'general-forms/$', views.general_forms, name='general-forms'),
    url(r'search-forms/$', views.search_forms, name='search-forms'),
    url(r'graph-forms/$', views.graph_forms, name='graph-forms'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'register/$', views.register, name='register'),
    # url(r'logout/$', views.logout, name='logout'),
    # url(r'blank/', views.blank, name='blank'),
]