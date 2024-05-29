from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import RedirectView

from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/')),
    path('home/' ,     include('home.urls') ),
    path('usermember/',include('usermember.urls')),
    path('news/'    ,  include('news.urls')),
    path('addproduct/'    ,  include('product.urls')),  
    path('orders/', include('orders.urls')), 
    
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
