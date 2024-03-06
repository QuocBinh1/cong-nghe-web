# models.py
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    # Thêm các trường khác tùy ý

    def __str__(self):
        return self.username
