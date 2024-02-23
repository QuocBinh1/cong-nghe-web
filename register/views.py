from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
from django.views import View


# Create your views here.
# class register(View):
def register(request):
    cf = contact_Form
    return render(request , 'register/dangki.html' , {'cf' : cf})

# def getRegister(request):
#     if request.method == "POST":
#         cf = contact_Form(request.method)
#         if cf.is_valid():
#             saveCF = contactForm(username = cf.cleaned_data['username']), 
#             email = cf.cleaned_data['email'], 
#             body = cf.cleaned_data['body'] 
#             saveCF.save()
#             return HttpResponse ("save thanh cong")
#     else:
#         return HttpResponse("luu that bai")
