from django.urls import path 
from . import views

app_name = 'news'
urlpatterns = [
    path('' , views.post_list_news , name = 'news'),
    path('<int:id>/' , views.postDetaill , name = 'postDetaill'),
    #path('saveRegister/' , views.saveRegister , name = "saveRegister")


]
