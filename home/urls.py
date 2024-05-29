#home/urls.py
from django.urls import path 
from product.models import Post , Comment
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import product_detail
app_name = 'home'
urlpatterns = [
    path('' , views.index , name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/<int:product_id>/', views.product_checkout, name='product_checkout'),
    path('profile_view/', views.profile_view, name='profile_view'),
    # path('cart/', views.cart, name='cart'),
    # path('other_product_detail/', views.other_product_detail, name='other_product_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
