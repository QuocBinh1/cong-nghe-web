#home/urls.py
from django.urls import path 
from blog.models import Post , Comment
from . import views
app_name = 'home'
urlpatterns = [
    path('' , views.index , name='home'),
    path('show-blog-posts/', views.show_blog_posts, name='show_blog_posts'),

    

]
