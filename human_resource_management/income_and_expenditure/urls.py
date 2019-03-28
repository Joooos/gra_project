from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    url(r'^income-entry/$', views.income_entry, name='income-entry'),
    url(r'^expenditure-entry/$', views.expenditure_entry, name='expenditure-entry'),
    url(r'^income-and-expenditure-details/$', views.income_and_expenditure_details, name='income-and-expenditure-details'),
]