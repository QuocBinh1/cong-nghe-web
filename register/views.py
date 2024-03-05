from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.shortcuts import render ,redirect
from django.http import HttpResponse



from .forms import register_Form , login_Form
from .models import register_models
from django.views import View


class registerView(View):
    def get(self , request):
        rf = register_Form()
        return render(request, 'register/dangki.html', {'rf': rf} )
    def post(self , request):
        rf = register_Form(request.POST)
        if rf.is_valid():
            savecf = register_models(username = rf.cleaned_data['username'],
                                email = rf.cleaned_data['email'],
                                password = rf.cleaned_data['password'] 
                                )
            savecf.save()
            # return redirect('home')  # Điều hướng sau khi đăng ký thành công
            return HttpResponse("dki thanh cong")
        else:
            return HttpResponse("dki khong thanh cong")
        




        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # if User.objects.filter(username=username).exists():
        #     return HttpResponse("Tên người dùng đã tồn tại")
        
        # user = User.objects.create_user(username , email , password)
        # return HttpResponse("save success")  
    
class loginView(View):
    def get(self , request):
        lf = login_Form
        return render(request, 'register/dangnhap.html', {'lf': lf} )
    def post(self , request):
        lf = login_Form(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
        
            user = authenticate(request, username = username , password = password)

            if user is not None:
                login(request, user)
                return redirect('home/trangchu.html')
            else:
                return render(request, 'register/dangnhap.html', {'lf': lf, 'error_message': 'Tên người dùng hoặc mật khẩu không đúng.'})
        else:
            return render(request, 'register/dangnhap.html', {'lf': lf})


