from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # url(r'^general-forms/$', views.general_forms, name='general-forms'),
    url(r'^bulletin-board/$', views.bulletin_board, name='bulletin-board'),
    url(r'^announcement-management/$', views.announcement_management, name='announcement-management'),
    url(r'^company-information/$', views.company_information, name='company-information'),
]