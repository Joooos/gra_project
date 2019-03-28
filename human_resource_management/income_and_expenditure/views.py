from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
import time
from django.forms import widgets
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Income_Entry_Form, Expenditure_Entry_Form


# Create your views here.
@login_required()
def income_entry(request):
    if request.method == "POST":
        income_date = request.POST.get('income_date')
        income_money = request.POST.get('income_money')
        income_type = request.POST.get('income_type')
        income_remark = request.POST.get('remark')

        timeStruct = time.strptime(income_date, "%m/%d/%Y")
        income_date = time.strftime("%Y-%m-%d", timeStruct)

        intry_income_form = Income_Entry_Form(income_time=income_date, income_salary=income_money, income_type=income_type,
                                              income_remark=income_remark)

        intry_income_form.save()
        message = "Save success!"

        return render(request, "income_and_expenditure/income-entry.html", {"message": message})


    elif request.method == "GET":
        return render(request, "income_and_expenditure/income-entry.html")


@login_required()
def expenditure_entry(request):
    if request.method == "POST":
        expenditure_date = request.POST.get('expenditure_date')
        expenditure_money = request.POST.get('expenditure_money')
        expenditure_type = request.POST.get('expenditure_type')
        expenditure_remark = request.POST.get('remark')

        timeStruct = time.strptime(expenditure_date, "%m/%d/%Y")
        expenditure_date = time.strftime("%Y-%m-%d", timeStruct)

        expenditure_income_form = Expenditure_Entry_Form(expenditure_time=expenditure_date, expenditure_salary=expenditure_money, expenditure_type=expenditure_type,
                                                        expenditure_remark=expenditure_remark)

        expenditure_income_form.save()
        message = "Save success!"

        return render(request, "income_and_expenditure/expenditure-entry.html", {"message": message})


    elif request.method == "GET":
        return render(request, "income_and_expenditure/expenditure-entry.html")


@login_required()
def income_and_expenditure_details(request):
    if request.method == "GET":
        items = []
        testlines = {}

        income_objects = Income_Entry_Form.objects.all()
        expenditure_objects = Expenditure_Entry_Form.objects.all()

        for income in income_objects:
            testlines['type'] = "支出"
            testlines['time'] = income.income_time
            testlines['salary'] = income.income_salary
            testlines['specific_type'] = income.income_type
            testlines['remark'] = income.income_remark
            items.append(testlines.copy())

        testlines = {}

        for epdt in expenditure_objects:
            testlines['type'] = "收入"
            testlines['time'] = epdt.expenditure_time
            testlines['salary'] = epdt.expenditure_salary
            testlines['specific_type'] = epdt.expenditure_type
            testlines['remark'] = epdt.expenditure_remark
            items.append(testlines.copy())

        return render(request, "income_and_expenditure/income-and-expenditure-details.html", {'items': items})
