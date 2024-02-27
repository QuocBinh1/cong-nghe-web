from django.urls import path 
from . import views
from models import postForm
app_name = 'news'
urlpatterns = [
    path('' , views.postForm.as_view() , name = 'news'),
    #path('saveRegister/' , views.saveRegister , name = "saveRegister")


]
