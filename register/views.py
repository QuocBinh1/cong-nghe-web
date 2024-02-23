from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form

# Create your views here.
def register(request):
    cf = contact_Form
    return render(request , 'register/dangki.html' , {'cf' : cf})

def getRengister(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse('save Thanh Cong')
    else:
        return HttpResponse('NOT POST')