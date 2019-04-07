from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, AuthUser
from .forms import RegistrationForm, UserForm
from django.contrib.auth import authenticate, logout, login

def index(request):
    return render(request, 'account/index.html')

# def registration(request):
#     # bool值，注册成功后改为 True
#     registered = False
#
#     # 如果是 http post 请求， 处理表单数据
#     if request.method == 'POST':
#         user_form = UserForm(data = request.POST)
#         profile_form = UserProfileForm(data = request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#
#             # 使用 set_password 方法计算密码哈希值
#             # 更新 user 对象
#             user.set_password(user.password)
#             user.save()
#
#             # 因为要自行处理 user 属性，所以设定 commit = False
#             # 延迟保存模型，以防出现完整性问题
#             profile = profile_form.save(commit=False)
#             profile.user = user
#
#
#             # 如果用户提供了头像，赋给 UserProfile 模型
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#
#             profile.save()
#
#             registered = True
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         # 不是 POST 请求，渲染两个 ModelForm 实例
#         # 表单为空，待用户填写
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#
#     return render(request, 'account/registration.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})

def register(request):
    # if request.session.get('is_login', None):
    #     return redirect("/index/")

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']

            if password1 != password2:
                message = "这两个密码不一致，请重试。"
                return render(request, 'account/registration.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = "已有人使用了该用户名，请尝试其他用户名。"
                    return render(request, 'account/registration.html', locals())

            # 使用内置 User 自带 create_user 方法创建用户，不需要使用 save()
            user = User.objects.create_user(username = username, password = password1, email=email, is_staff=1)

            # 如果直接使用 objects.create()方法后不需要使用 save()
            # user_profile = UserProfile(user = user)
            # user_profile.save()

            return HttpResponseRedirect("/account/login/")  # 自动跳转到登录界面

    else:
        register_form = RegistrationForm()

    return render(request, 'account/registration.html', locals())




def user_login(request):

    # if request.session.get('is_login', None):
    #     return HttpResponseRedirect(reverse('bulletin-board'))

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['is_login'] = True
                request.session['user_name'] = username
                request.session.set_expiry(0)
                is_remembered = request.POST.get('rememberMe')
                response = HttpResponseRedirect(reverse('bulletin-board'))
                if is_remembered:
                    response.set_cookie('username', username)
                else:
                    response.set_cookie('username', '')
                request.session['username'] = username
                return response
            else:
                # print(username, password)
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'account/login.html', locals())


def profile(request):
    return render(request, 'account/profile.html', locals())

@login_required()
def user_logout(request):
    # pass
    logout(request)
    request.session.flush()
    # return HttpResponseRedirect(reverse('login'))
    # return redirect('/index/')
    return HttpResponseRedirect("/account/login/")
    # return render(request, 'account/index.html')
    # return render(request, 'account/login.html')