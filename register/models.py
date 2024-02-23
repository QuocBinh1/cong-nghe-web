from django.db import models

# Create your models here.
class contactForm(models.Model):
    username = models.CharField(max_length = 25)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self): # hien ra ten o admin (de nhan biet)
        return self.username 