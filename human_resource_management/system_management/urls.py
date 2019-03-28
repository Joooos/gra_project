from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # url(r'^general-forms/$', views.general_forms, name='general-forms'),
    url(r'^bulletin-board/$', views.bulletin_board, name='bulletin-board'),
]