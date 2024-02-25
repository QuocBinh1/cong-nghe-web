from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm

def register(request):
    cf = contact_Form
    return render(request, 'register/dangki.html', {'cf': cf} )
def saveRegister(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            savecf = contactForm(
                username = cf.cleaned_data['username'],
                email = cf.cleaned_data['email'],
                body = cf.cleaned_data['body']
            )
            savecf.save()
            return HttpResponse("luu thanh cong")
        else:
            return HttpResponse("Dữ liệu không hợp lệ")

    else:
        return HttpResponse ("khong luu dcuo")