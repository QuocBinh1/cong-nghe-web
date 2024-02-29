from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
from django.views import View


class register(View):
    def get(self , request):
        cf = contact_Form
        return render(request, 'register/dangki.html', {'cf': cf} )
    def post(self , request):
        if request.method == "POST":
            cf = contact_Form(request.POST)
            if cf.is_valid():
                savecf = contactForm(
                    username = cf.cleaned_data['username'],
                    email = cf.cleaned_data['email'],
                    password = cf.cleaned_data['password']
                )
                savecf.save()
                return HttpResponse("luu thanh cong")
            else:
                return HttpResponse("Dữ liệu không hợp lệ")

        else:
            return HttpResponse ("khong luu dcuo")
