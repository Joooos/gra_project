from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
import datetime
import pytz
from pytz import timezone


# Create your views here.
def bulletin_board(request):
    cst_tz = timezone('Asia/Shanghai')
    year = datetime.datetime.now().replace(tzinfo=cst_tz).year
    month = datetime.datetime.now().replace(tzinfo=cst_tz).month
    day = datetime.datetime.now().replace(tzinfo=cst_tz).day
    hour = datetime.datetime.now().replace(tzinfo=cst_tz).hour
    minute = datetime.datetime.now().replace(tzinfo=cst_tz).minute
    weekday = datetime.datetime.now().replace(tzinfo=cst_tz).isoweekday()
    day_or_night = ""
    if(weekday == 1):
        weekday = "Mon."
    elif(weekday == 2):
        weekday = "Tue."
    elif (weekday == 3):
        weekday = "Wed."
    elif (weekday == 4):
        weekday = "Thu."
    elif (weekday == 5):
        weekday = "Fri."
    elif (weekday == 6):
        weekday = "Sat."
    elif (weekday == 7):
        weekday = "Sun."

    if(month == 1):
        month = "January"
    elif(month == 2):
        month = "February"
    elif (month == 3):
        month = "March"
    elif (month == 4):
        month = "April"
    elif (month == 5):
        month = "May"
    elif (month == 6):
        month = "June"
    elif (month == 7):
        month = "July"
    elif (month == 8):
        month = "August"
    elif (month == 9):
        month = "September"
    elif (month == 10):
        month = "October"
    elif (month == 11):
        month = "November"
    elif (month == 12):
        month = "December"

    if(hour <= 12):
        day_or_night = "AM"
    else:
        day_or_night = "PM"

    month_and_day = month + " " + str(day)
    year_and_weekday = str(year) + ", " + weekday
    return render(request, "system_management/bulletin-board.html", {"month_and_day": month_and_day, "year_and_weekday": year_and_weekday
                                                                     , "day_or_night": day_or_night })



def announcement_management(request):
    return render(request, "system_management/announcement-management.html", )

def company_information(request):
    return render(request, "system_management/company-information.html", )