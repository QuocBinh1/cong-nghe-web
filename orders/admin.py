from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'name', 'sdt', 'shipping_address', 'order_status', 'payments', 'created_at')
    list_filter = ('order_status', 'payments', 'created_at')
    search_fields = ('user__username', 'email', 'name', 'sdt')

    # Exclude non-editable fields from the form
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Order, OrderAdmin)
