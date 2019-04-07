from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
import time
from django.forms import widgets
from django import forms
from account.forms import SelectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def new_job_list(request):
    # return render(request, "worklist/new-job-list.html", )
    if request.method == "POST":
        # real_name = request.POST.get('sel_value', "")  # 这里可以取到下拉表单中的值
        # # 接下来就是保存数值与其他逻辑了
        # year = request.POST.get('year')
        # month = request.POST.get('month')
        # department = request.POST.get('department')
        # basic_salary = request.POST.get('basic_salary')
        # phone_allowance = request.POST.get('phone_allowance')
        # overtime_days = request.POST.get('overtime_days')
        # overtime_salary = request.POST.get('overtime_salary')
        # absence_days = request.POST.get('absence_days')
        # absence_salary = request.POST.get('absence_salary')
        # other_deduction = request.POST.get('other_deduction')
        # other_withholding = request.POST.get('other_withholding')
        # personal_income_tax = request.POST.get('personal_income_tax')
        #
        # payroll_entry_form = Payroll_Entry_Form(year=year, real_name=real_name, department=department, month=month,
        #                                         basic_salary=basic_salary, phone_allowance=phone_allowance,
        #                                         overtime_days=overtime_days, overtime_salary=overtime_salary,
        #                                         absence_days=absence_days, absence_salary=absence_salary,
        #                                         other_deduction=other_deduction,
        #                                         other_withholding=other_withholding,
        #                                         personal_income_tax=personal_income_tax
        #                                         )
        # payroll_entry_form.save()
        message = "Success!"

        return HttpResponse("Success!")

        # else:
        #     # 表单验证未通过的逻辑,多半要重新填写或直接给个404
        #     return HttpResponse("Invalid.")

    elif request.method == "GET":
        select_form = SelectForm()
        return render(request, 'worklist/new-job-list.html', {'select_form': select_form, })


@login_required()
def worklist_summary(request):
    return render(request, "worklist/worklist-summary.html", )