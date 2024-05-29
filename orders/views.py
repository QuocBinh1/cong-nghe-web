# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from product.models import Post

@login_required
def create_order(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Post, id=product_id)
        title = product.title
        price = product.price
        quantity = int(request.POST.get('quantity', 1))
        payments = request.POST.get('payments')  # Lấy giá trị phương thức thanh toán

        order = Order(
            user=user,
            email=request.POST.get('email', ''),
            name=request.POST.get('name', ''),
            sdt=request.POST.get('sdt', ''),
            shipping_address=request.POST.get('shipping_address', ''),
            shipping_city=request.POST.get('shipping_city', ''),
            shipping_district=request.POST.get('shipping_district', ''),
            shipping_ward=request.POST.get('shipping_ward', ''),
            note=request.POST.get('note', ''),
            order_status=request.POST.get('order_status', 'processing'),
            product=product,
            title=title,
            quantity=quantity,
            price=price,
            payments=payments,
        )
        order.save()
        return redirect('orders:order_created', order_id=order.id)  # Chuyển hướng với order_id
    return render(request, 'orders/checkout.html')

def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_created.html', {'order': order}) 

def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})
