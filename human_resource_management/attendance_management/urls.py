from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    # url(r'^general-forms/$', views.general_forms, name='general-forms'),
    url(r'^checkin-and-out/$', views.checkin_and_out, name='checkin-and-out'),
    url(r'^ask-for-leave/$', views.ask_for_leave, name='ask-for-leave'),
    url(r'^attendance-check/$', views.attendance_check, name='attendance-check'),
    url(r'^leave-statistics/$', views.leave_statistics, name='leave-statistics'),
    url(r'^overtime-statistics/$', views.overtime_statistics, name='overtime-statistics'),
]