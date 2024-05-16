#blog/models.py
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.utils import timezone
import pytz
from django.db.models import Sum
from datetime import date


class Post(models.Model):
    TYPE_CHOICES = [('laptop', 'Laptop'),('phone', 'Phone'),('tablet', 'Tablet'),('other', 'Other')]  # Lựa chọn 'Khác'
    TRADEMARK_CHOICES = [('asus', 'Asus'),('dell', 'Dell'),('hp', 'HP'),('lenovo', 'Lenovo'),('samsung', 'Samsung'),('apple', 'Apple'),('other', 'Other')]  # Lựa chọn 'Khác'
    id = models.AutoField(primary_key=True)  # Đây là trường ID tự tăng
    author = models.ForeignKey(User, on_delete=models.CASCADE) #người thêm 
    title = models.CharField(max_length=100) #tiêu đề
    description = models.TextField() #mô tả
    price = models.DecimalField(max_digits=10 , decimal_places=0) #giá
    quantity = models.CharField(max_length=3) # số lượng 
    category = models.CharField(max_length=20, choices=TYPE_CHOICES) # loại
    trademark = models.CharField(max_length=20, choices=TRADEMARK_CHOICES)#Thương hiệu
    timestamp = models.DateTimeField(auto_now_add=True)  # Thêm trường timestamp vào mô hình Post
    image = models.ImageField(upload_to='post_images/')
    
    def get_absolute_url(self):
        return reverse('blog')
    #định dạng dấu chấm của giá
    @property
    def price_formatted(self):
        return '{:,.0f}'.format(self.price)
    @classmethod
    def total_price(cls):
        total_price = cls.objects.aggregate(total_price=Sum('price'))
        return total_price['total_price']

class ActionHistory(models.Model):
    ACTION_CHOICES = [
        ('add', 'Add'),
        ('delete', 'Delete'),
        ('update', 'Update'),
    ]
    id = models.AutoField(primary_key=True)  # Đây là trường ID tự tăng
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    post_title = models.CharField(max_length=100, null=True, blank=True)
    post_description = models.TextField(null=True, blank=True)
    post_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    post_quantity = models.CharField(max_length=3, null=True, blank=True)
    post_category = models.CharField(max_length=20, null=True, blank=True)
    post_trademark = models.CharField(max_length=20, null=True, blank=True)
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
 
    timestamp = models.DateTimeField(auto_now_add=True)
   

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
