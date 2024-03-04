from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse



from .forms import register_Form , login_Form
from .models import register_models
from django.views import View


class registerView(View):
    def get(self , request):
        rf = register_Form
        return render(request, 'register/dangki.html', {'rf': rf} )
    def post(self , request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Tên người dùng đã tồn tại")
        
        user = User.objects.create_user(username , email , password)
        
        return HttpResponse("save success")  
    



class loginView(View):
    def get(self , request):
        lf = login_Form
        return render(request, 'register/dangnhap.html', {'lf': lf} )
    def post(self , request):
        username = request.POST['username']
        password = request.POST['password']

        

        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return HttpResponse("login success")
        else:
            return HttpResponse("login fall")



