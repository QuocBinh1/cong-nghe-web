from django.db import models

# Create your models here.
class postForm(models.Model):
    title = models.CharField( max_length=255)
    body = models.TextField()
    img = models.ImageField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # hien ra ten o admin (de nhan biet)
        return self.title