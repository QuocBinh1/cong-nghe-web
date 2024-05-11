from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.core.paginator import Paginator
from .models import Product
def index(request):
    # return HttpResponse('hello')
    posts = Post.objects.all()
    return render(request , 'home/trangchu.html', {'posts': posts})

def product_detail(request, product_id):
    # Lấy thông tin chi tiết của sản phẩm từ database
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'home/product_detail.html', {'product': product})

def other_product_detail(request):
    context = {}
    return render(request , 'home/product_detail.html' , context)

def cart(request):
    context = {}
    return render(request , 'home/cart.html' , context)
