#product/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.utils import timezone
import pytz
from django.db.models import Sum, F
from datetime import date

User = get_user_model()

class Post(models.Model):
    TYPE_CHOICES = [('laptop', 'Laptop'), ('phone', 'Phone'), ('tablet', 'Tablet'), ('other', 'Other')]
    TRADEMARK_CHOICES = [('asus', 'Asus'), ('dell', 'Dell'), ('hp', 'HP'), ('lenovo', 'Lenovo'), ('samsung', 'Samsung'), ('apple', 'Apple'), ('other', 'Other')]

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)
    trademark = models.CharField(max_length=20, choices=TRADEMARK_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/')

    def get_absolute_url(self):
        return reverse('blog')

    @property
    def price_formatted(self):
        return '{:,.0f}'.format(self.price)

    @classmethod
    def total_quantity_by_category(cls):
        total_quantity_by_category = cls.objects.values('category').annotate(total_quantity=Sum('quantity'))
        return total_quantity_by_category

    @classmethod
    def total_quantity_with_details(cls):
        total_quantity_with_details = cls.objects.values('category').annotate(
            category_name=F('category'),
            total_quantity=Sum('quantity'),
            description=F('description'),
            titles=F('title'),
            quantities=F('quantity')
        )
        return total_quantity_with_details

class ActionHistory(models.Model):
    ACTION_CHOICES = [
        ('add', 'Add'),
        ('delete', 'Delete'),
        ('update', 'Update'),
    ]

    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    # post = models.ForeignKey(Post, on_delete=models.SET_NULL)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,null=True, blank=True)  # Đảm bảo trường này không cho phép null
    post_title = models.CharField(max_length=100, null=True, blank=True)
    post_description = models.TextField(null=True, blank=True)
    post_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    post_quantity = models.CharField(max_length=3, null=True, blank=True)
    post_category = models.CharField(max_length=20, null=True, blank=True)
    post_trademark = models.CharField(max_length=20, null=True, blank=True)
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

class ActivityHistory(models.Model):
    TYPE_CHOICES = [('laptop', 'Laptop'), ('phone', 'Phone'), ('tablet', 'Tablet'), ('other', 'Other')]
    TRADEMARK_CHOICES = [('asus', 'Asus'), ('dell', 'Dell'), ('hp', 'HP'), ('lenovo', 'Lenovo'), ('samsung', 'Samsung'), ('apple', 'Apple'), ('other', 'Other')]

    description = models.TextField()
    category = models.CharField(max_length=20, null=True, blank=True, choices=TYPE_CHOICES)
    trademark = models.CharField(max_length=20, null=True, blank=True, choices=TRADEMARK_CHOICES)
    total_quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def update_quantity_totals(cls):
        post_totals = Post.total_quantity_by_category()

        for category_total in post_totals:
            category = category_total['category']
            total_quantity = category_total['total_quantity']
            activity_history, _ = cls.objects.get_or_create(category=category)
            activity_history.total_quantity = total_quantity
            activity_history.save()
