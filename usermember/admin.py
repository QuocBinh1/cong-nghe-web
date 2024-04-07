from django.contrib import admin
from .models import CustomUser
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'password']
    # pass

# admin.site.register(CustomUser)