from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/')),
    path('home/' ,     include('home.urls')),
    path('register/' , include('register.urls')),
    path('login/'    , include('login.urls')),


]
