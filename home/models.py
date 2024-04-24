# models.py

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    # Định nghĩa các trường khác cho sản phẩm tại đây (ví dụ: giá, số lượng, v.v.)

    def __str__(self):
        return self.title
