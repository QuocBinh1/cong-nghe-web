from django.contrib import admin
from .models import postForm
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' ,'body' , 'img']
    search_fields = ['title']
    # inlines = [CommentInline]
admin.site.register(postForm)