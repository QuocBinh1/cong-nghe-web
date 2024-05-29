# orders/models.py
from django.db import models
from django.contrib.auth.models import User
from product.models import Post 
from decimal import Decimal
class Order(models.Model):
    ORDER_STATUS_CHOICES = [('processing', 'Processing'),('shipped', 'Shipped'),('delivered', 'Delivered'),('cancelled', 'Cancelled')]
    PAYMENT_CHOICES = [('cod', 'COD'), ('bank transfer', 'Bank Transfer')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255 , default='')
    name = models.CharField(max_length=255 ,null=True)
    sdt = models.CharField(max_length=15)
   
    shipping_city = models.CharField(max_length=100)
    shipping_district = models.CharField(max_length=100)
    shipping_ward = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='processing')
    payments = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='cod')

    product = models.ForeignKey(Post, on_delete=models.CASCADE)  
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/' ,blank=True, null=True)
    # def __str__(self):
    #     return f"mã đơn : {self.id} ; Họ Và Tên : {self.name} ; SDT : {self.sdt} thời gian đặt : {self.created_at}"
    def save(self, *args, **kwargs):
        # Chuyển đổi quantity và price thành các kiểu số, xử lý các lỗi chuyển đổi có thể xảy ra
        try:
            self.quantity = int(self.quantity)  # Chuyển đổi quantity thành số nguyên
            self.price = Decimal(self.price)    # Chuyển đổi price thành số thập phân
        except (ValueError, TypeError):
            pass  # Bỏ qua các lỗi chuyển đổi và tiếp tục với các giá trị mặc định
        # Kiểm tra xem cả quantity và price có giá trị hợp lệ không
        if self.quantity is not None and self.price is not None:
            # Tính toán total_price dựa trên quantity và price
            self.total_price = self.quantity * self.price
        else:
            # Đặt total_price thành None nếu một trong số quantity hoặc price bị thiếu
            self.total_price = None
        # Gọi phương thức save() của lớp cha để lưu đối tượng
        super().save(*args, **kwargs)


