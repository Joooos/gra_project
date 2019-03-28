from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    url(r'^payroll-entry/$', views.payroll_entry, name='payroll-entry'),

]