from django.shortcuts import render
from django.http import HttpResponse
from .models import postForm
from django.views import View
# Create your views here.

def post_list_news(request):
    pf  = postForm.objects.all()
    return render(request , 'news/tintuc.html',{'pf':pf } )
def postDetaill(request, id):
    pd = postForm.objects.get(id = id)  
    return render(request , 'news/postDetaill.html',{'pd':pd } )
