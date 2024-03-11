# models.py
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.username
