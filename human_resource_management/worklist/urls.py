from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # url(r'^general-forms/$', views.general_forms, name='general-forms'),
    url(r'^new-job-list/$', views.new_job_list, name='new-job-list'),
    url(r'^worklist-summary/$', views.worklist_summary, name='worklist-summary'),
]