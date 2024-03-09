# usermember/urls.py
from django.urls import path
from . import views

app_name = 'usermember'

urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('register/', views.register_view.as_view(), name='register'),
    
]
