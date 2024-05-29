#home/views.py
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from product.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from orders.models import Order

def index(request):
    # return HttpResponse('hello')
    posts = Post.objects.all()
    return render(request , 'home/trangchu.html', {'posts': posts})

def product_detail(request, product_id):
    # Lấy thông tin chi tiết của sản phẩm từ database
    product = get_object_or_404(Post, id=product_id)
    return render(request, 'home/product_detail.html', {'product': product})

def product_checkout(request, product_id):
    product_checkout = get_object_or_404(Post, id=product_id)
    return render(request, 'orders/checkout.html', {'product_checkout': product_checkout})

def profile_view(request, product_id):
    profile = get_object_or_404(User, id=product_id)
    return render(request, 'home/profile.html', {'profile': profile})



def cart_icon(request):
    user = request.user
    order_count = Order.objects.filter(user=user).count() if user.is_authenticated else 0
    return {'order_count': order_count}
