"""human_resource_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from account import views as account

urlpatterns = [
    url(r'^$', account.register),
    url(r'^account/', include('account.urls')),
    url(r'^employee_information/', include('employee_information.urls')),
    url(r'^payroll_management/', include('payroll_management.urls')),
    url(r'^system_management/', include('system_management.urls')),
    url(r'^attendance_management/', include('attendance_management.urls')),
    url(r'^worklist/', include('worklist.urls')),
    url(r'^income_and_expenditure/', include('income_and_expenditure.urls')),
    url(r'^admin/', admin.site.urls),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

