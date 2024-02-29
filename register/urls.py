from django.urls import path 
from . import views
app_name = 'register'
urlpatterns = [
    path('register/' , views.register.as_view() , name = 'register'),    
    path('login/' , views.loginView.as_view() , name = 'login'),


]
