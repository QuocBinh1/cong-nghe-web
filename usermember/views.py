# views.py
from django.urls import reverse
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import CustomUser


from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin   #class base-view
from django.contrib.auth.models import User



class register_view(View):
    def get(self , request):
        form = RegisterForm()
        return render(request, 'usermember/register.html', {'form': form} )
    def post(self , request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            # Kiểm tra xem người dùng đã tồn tại hay không
            if User.objects.filter(username=username).exists():
                messages.error(request, "Tên người dùng đã tồn tại")
                return redirect('usermember:register')
            elif password1 != password2:
                messages.error(request, "Mật khẩu không khớp")
                return redirect('usermember:register')
            else:
                user = User.objects.create_user(username=username,email=email, password=password1)
                messages.success(request, 'Đăng ký thành công')
                login_url = reverse('usermember:login')  # Xác định URL của trang đăng nhập
                return redirect(login_url)  # Chuyển hướng đến trang đăng nhập
        else:
            messages.error(request, 'Dữ liệu không hợp lệ')
            return redirect('usermember:register')
 

class login_view(View):
    def get(self , request):
        form = LoginForm()
        return render(request, 'usermember/login.html', {'form': form} )
    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #dữ liệu trong form
            password = form.cleaned_data['password']#dữ liệu trong form
            try:
                user = authenticate(request, username = User.objects.get(email=username) , password = password)
            except:
                user = authenticate(request, username = username , password = password)
            # return HttpResponse(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'dang nhap thanh congg')
                return render(request, 'usermember/private.html')
            else:
                messages.error(request, "dang nhap that bai")
                return redirect('usermember:login')
        else:
            messages.error(request, 'du lieu khong hop le')
            return redirect('usermember:login')
@login_required
def logout_view(request):
    logout(request)
    return redirect('usermember:login')
    # return HttpResponse('ban da dang xuat ')  

#dung cho class base-view
class privatePage(LoginRequiredMixin, View):
    login_url = '/usermember/login/'  # Định nghĩa URL cho trang đăng nhập
    # redirect_field_name = 'redirect_to'  # Tên trường chứa URL chuyển hướng sau khi đăng nhập

    def get(self, request):
        return render(request, 'usermember/private.html')


