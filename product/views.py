from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.forms import BlogPostForm
from .models import *
import pytz

@login_required(login_url = '/login')
def add_product(request):
    form = BlogPostForm()
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "product/addproduct.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "product/addproduct.html", {'form':form})
