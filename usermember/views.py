# views.py
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import CustomUser


from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate , login 
from django.contrib.auth.models import User



class register_view(View):
    def get(self , request):
        form = RegisterForm()
        return render(request, 'usermember/register.html', {'form': form} )
    def post(self , request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Kiểm tra xem người dùng đã tồn tại hay không
            if User.objects.filter(username=username).exists():
                messages.error(request, "Tên người dùng đã tồn tại")
                return redirect('usermember:register')
            else:
                user = User.objects.create_user(username=username, password=password)
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
            user = authenticate(request, username = username , password = password)
            # return HttpResponse(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'dang nhap thanh congg')
                return redirect('home:home')
            else:
                messages.error(request, "dang nhap that bai")
                return redirect('usermember:login')
            
        else:
            messages.error(request, 'du lieu khong hop le')
            return redirect('usermember:register')
        
def my_view(request):
    # Các công việc khác ở đây
    some_condition = True
    # Hiển thị thông báo
    if some_condition:
        return render(request, 'my_template.html', {'show_alert': True, 'alert_type': 'success', 'alert_message': 'Thành công!'})
    else:
        return render(request, 'my_template.html', {'show_alert': True, 'alert_type': 'error', 'alert_message': 'Lỗi!'})




