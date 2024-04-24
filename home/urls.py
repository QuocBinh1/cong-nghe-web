#home/urls.py
from django.urls import path 
from blog.models import Post , Comment
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'home'
urlpatterns = [
    path('' , views.index , name='home'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('other_product_detail/', views.other_product_detail, name='other_product_detail'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
