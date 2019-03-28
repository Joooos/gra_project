from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import re
from django.forms import widgets
from account import models
import json

def email_check(email):
    pattern = re.compile(r"\"?([a-zA-Z0-9.?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

# class RegistrationForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # email = forms.EmailField(label='Email')
#     password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Password Confirmation', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     # Use distinguish methods to define custom validation rules
#
#     def distinguish_username(self):
#         username = self.cleaned_data.get('username')
#
#         if len(username) < 6:
#             raise forms.ValidationError("Your username must be at least 6 characters long.")
#         elif len(username) > 50:
#             raise forms.ValidationError("Your username is too long.")
#         else:
#             filter_result = User.objects.filter(username_exact = username)
#             if len(filter_result) > 0:
#                 raise forms.ValidationError("Your username already exists.")
#
#         return username
#
#     def distinguish_email(self):
#         email = self.cleaned_data.get('email')
#
#         if email_check(email):
#             filter_result = User.objects.filter(email_exact = email)
#             if len(filter_result) > 0:
#                 raise forms.ValidationError("Your email already exists.")
#         else:
#             raise forms.ValidationError("Please enter a valid email.")
#
#         return email
#
#     def distinguish_password1(self):
#         password1 = self.cleaned_data.get('password1')
#
#         if len(password1) < 6:
#             raise forms.ValidationError("Your password is too short.")
#         elif len(password1) > 20:
#             raise forms.ValidationError("Your password is too long.")
#
#         return password1
#
#
#     def distinguish_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Password mismatch. Please enter again.")
#
#         return password2

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SelectTestForm(forms.Form):
    SELVALUE = (
        ('标题', 'first'),
        ('内容', 'second'),
        ('作者', 'third'),
    )
    # SELVALUE = models.UserProfile.objects.values_list("real_name")
    # SELVALUE2 = models.UserProfile.objects.values_list("id","real_name")
    # print(SELVALUE2)
    # print(list(SELVALUE2))
    # print(str(list(SELVALUE2)))
    # print(eval(str(list(SELVALUE2))))
    # for i in SELVALUE2:
    #     print(i)
    #     print(type(i))
    #     print(len(SELVALUE2))
    json_list = []
    userprofiles = models.UserProfile.objects.all()
    for userprofile in userprofiles:
        json_dict = {}
        json_dict["real_name"] = userprofile.real_name
        json_list.append(json_dict)
    print(json_list)
    print(type(json_list))
    print(json.dumps(json_list))
    print(type(json.dumps(json_list)))
    real_name_list = []
    for item in json_list:
        for key in item:
            real_name_list.append(item[key])
    print(real_name_list)
    sel_value = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=json_list))


















































class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    # Meta 类提供额外的属性
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )