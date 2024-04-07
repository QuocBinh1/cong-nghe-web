from django.contrib import admin
from .models import Comment , Post
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','description','content','image' ,'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

admin.site.register(Post,PostAdmin)