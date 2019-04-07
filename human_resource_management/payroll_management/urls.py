from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    url(r'^payroll-entry/$', views.payroll_entry, name='payroll-entry'),
    url(r'^analysis-of-wage-costs/$', views.analysis_of_wage_costs, name='analysis-of-wage-costs'),

]