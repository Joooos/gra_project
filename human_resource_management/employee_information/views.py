from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile
import time
import datetime
from django.contrib.auth.decorators import login_required
import json


# Create your views here.

@login_required()
def general_forms(request):
    # return render(request, 'employee_information/general-forms.html')
    if request.method == "POST":
        account_number = request.POST.get('account_number')
        real_name = request.POST.get('real_name')
        department = request.POST.get('department')
        position = request.POST.get('position')
        starting_date = request.POST.get('starting_date')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        education = request.POST.get('education')
        gender = request.POST.get('gender')
        personal_id = request.POST.get('personal_id')
        is_inservice = request.POST.get('is_inservice')
        political_status = request.POST.get('political_status')
        cellphone = request.POST.get('cellphone')
        office_number = request.POST.get('office_number')
        office_email = request.POST.get('office_email')
        remark = request.POST.get('remark')
        user_id = request.POST.get('user_id')

        timeStruct = time.strptime(starting_date, "%m/%d/%Y")
        starting_date = time.strftime("%Y-%m-%d", timeStruct)
        timeStruct = time.strptime(date_of_birth, "%m/%d/%Y")
        date_of_birth = time.strftime("%Y-%m-%d", timeStruct)

        # 性别
        if gender == "male":
            gender = 1
        else:
            gender = 0

        # print(request.user.id)
        # print(request.user.username)
        # user = User.objects.get(username = request.user)
        # user_profile = UserProfile.objects.get(user_id=request.user.id)
        user_profile = UserProfile(account_number=account_number, real_name=real_name, department=department,personal_id = personal_id,
                                   position=position, starting_date=starting_date, date_of_birth=date_of_birth, age=age,
                                   education=education, gender=gender, is_inservice=is_inservice, political_status=political_status,
                                   cellphone=cellphone, office_number=office_number, office_email=office_email, remark=remark,
                                   user_id=user_id)
        user_profile.save()
        message = "Success!"

        return render(request, 'employee_information/general-forms.html')

    elif request.method == "GET":
        message = 0
        return render(request, 'employee_information/general-forms.html', locals())

def search_forms(request):
    if request.method == "GET":

        items = []
        testlines = {}

        context = UserProfile.objects.all()
        for c in context:
            testlines['real_name'] = c.real_name
            testlines['account_number'] = c.account_number
            testlines['department'] = c.department
            testlines['age'] = c.age
            testlines['starting_date'] = c.starting_date
            testlines['date_of_birth'] = c.date_of_birth
            testlines['education'] = c.education
            testlines['gender'] = c.gender
            testlines['is_inservice'] = c.is_inservice
            testlines['political_status'] = c.political_status
            testlines['cellphone'] = c.cellphone
            testlines['office_email'] = c.office_email
            testlines['personal_id'] = c.personal_id
            testlines['remark'] = c.remark
            items.append(testlines.copy())

        return render(request, 'employee_information/search-forms.html', {'items': items})

def graph_forms(request):

    items = []
    testlines = {}
    borntimes = []
    gender_man = 0
    gender_woman = 0


    # 获取员工性别信息
    context = UserProfile.objects.all()
    for c in context:
        testlines['gender'] = c.gender
        if testlines['gender'] == True:
            gender_man += 1
        else:
            gender_woman += 1
    print(gender_man)
    print(gender_woman)
    percent_man = float(gender_man)/(gender_man + gender_woman)
    percent_woman = float(gender_woman)/(gender_man + gender_woman)

    # 获取员工生日信息
    for c in context:
        borntimes.append(c.date_of_birth)

    t80 = datetime.datetime(1980, 1, 1, 0, 0, 0, 0)
    t90 = datetime.datetime(1990, 1, 1, 0, 0, 0, 0)
    t70 = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)

    n70 = 0.0
    n80 = 0.0
    n90 = 0.0

    for i in range(0, len(borntimes)):
        testline = borntimes[i]
        testline = testline.replace(tzinfo=None)
        print(testline)
        if(testline >= t90):
            n90 += 1
        elif(testline >= t80):
            n80 += 1
        elif(testline >= t70):
            n70 += 1

    percent_after_seven = float((n70)/(n70 + n80 + n90))
    percent_after_eight = float((n80)/(n70 + n80 + n90))
    percent_after_nine = float((n90)/(n70 + n80 + n90))


    # 获取部门人数
    department_num = []
    percent_depart = []
    num_of_finan = 0
    num_of_tech = 0
    num_of_person = 0
    num_of_project = 0
    num_of_market = 0
    num_of_sales = 0

    for c in context:
        department = c.department
        if department == "人事部":
            num_of_person += 1
        elif department == "财务部":
            num_of_finan += 1
        elif department == "技术部":
            num_of_tech += 1
        elif department == "项目部":
            num_of_project += 1
        elif department == "市场部":
            num_of_market += 1
        elif department == "销售部":
            num_of_sales +=1

    department_num.append(["人事部", num_of_person])
    department_num.append(["财务部", num_of_finan])
    department_num.append(["技术部", num_of_tech])
    department_num.append(["项目部", num_of_project])
    department_num.append(["市场部", num_of_market])
    department_num.append(["销售部", num_of_sales])

    print(department_num)

    total = num_of_sales + num_of_market + num_of_project + num_of_tech + num_of_finan + num_of_person

    percent_of_person = float(num_of_person)/total
    percent_of_finan = float(num_of_finan)/total
    percent_of_tech = float(num_of_tech)/total
    percent_of_project = float(num_of_project)/total
    percent_of_market = float(num_of_market)/total
    percent_of_sales = float(num_of_sales)/total

    percent_depart.append(percent_of_person)
    percent_depart.append(percent_of_finan)
    percent_depart.append(percent_of_tech)
    percent_depart.append(percent_of_project)
    percent_depart.append(percent_of_market)
    percent_depart.append(percent_of_sales)

    return render(request, 'employee_information/graph-forms.html', {"percent_man": json.dumps(percent_man), "percent_woman": json.dumps(percent_woman),
                                                                     "percent_after_seven": json.dumps(percent_after_seven), "percent_after_eight": json.dumps(percent_after_eight),
                                                                     "percent_after_nine": json.dumps(percent_after_nine), "department_num": json.dumps(department_num),
                                                                     "percent_depart": json.dumps(percent_depart)})