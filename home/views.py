from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # return HttpResponse('hello')
    return render(request , 'home/trangchu.html')
