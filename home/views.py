from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post , Comment
def index(request):
    # return HttpResponse('hello')
    return render(request , 'home/trangchu.html')
def show_blog_posts(request):
    # Truy vấn tất cả các bài đăng từ bảng blog_post
    blog_posts = Post.objects.all()
    return render(request, 'home/show_blog_posts.html', {'blog_posts': blog_posts})
