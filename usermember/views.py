# views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import CustomUser
from django.views import View
from django.contrib.auth import authenticate , login

from django.http import HttpResponse

class register_view(View):
    def get(self , request):
        form = RegisterForm()
        return render(request, 'usermember/register.html', {'form': form} )
    def post(self , request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            savecf = CustomUser(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'] 
                                )
            savecf.save()
            return HttpResponse("dki thanh cong")
        else:
            return HttpResponse("dki khong thanh cong")
        

class login_view(View):
    def get(self , request):
        form = LoginForm
        return render(request, 'usermember/login.html', {'form': form} )
    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #dữ liệu trong form
            password = form.cleaned_data['password']#dữ liệu trong form
            user = authenticate(request, username = username , password = password)
            # return HttpResponse(user)
            if user is not None:
                login(request, user)
                return HttpResponse('dang nhap thanh cong')
            else:
                return HttpResponse("dang nhap that bai")
                # return render(request, 'usermember/login.html', {'form': form, 'error_message': 'Tên người dùng hoặc mật khẩu không đúng.'})
        else:
            return render(request, 'usermember/login.html', {'form': form})
