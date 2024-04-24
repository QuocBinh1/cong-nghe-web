from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('blog')
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    