# home/context_processors.py
from orders.models import Order

def cart_icon(request):
    user = request.user
    order_count = Order.objects.filter(user=user).count() if user.is_authenticated else 0
    return {'order_count': order_count}
