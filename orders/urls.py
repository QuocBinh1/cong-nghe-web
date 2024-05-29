from django.urls import path
from . import views
app_name = 'orders'  
urlpatterns = [
    # path('orders/', views.OrderListView.as_view(), name='order-list'),
    # path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_created/<int:order_id>/', views.order_created, name='order_created'),  # Thêm đường dẫn cho order_created.html
    path('order_history/', views.order_history, name='order_history'),


]
