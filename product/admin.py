#admin.py
from django.contrib import admin
from .models import Comment , Post ,ActionHistory ,ActivityHistory
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','price','quantity','category','trademark' ,'timestamp','image']
    list_filter = ['timestamp' ,'category', 'trademark']
    search_fields = [ 'title','category', 'trademark']
    inlines = [CommentInline]

    
class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = ('action', 'post_title', 'post_price', 'post_quantity', 'post_category', 'post_trademark','timestamp')
    list_filter = ('action', 'timestamp' , 'post_trademark', 'post_category' ) 
    search_fields = ('post_title', 'action', 'post_trademark', 'post_category' )
    
class ActivityHistoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'total_quantity' , 'timestamp','description']
    list_filter = ( 'timestamp' , 'category', 'total_quantity' )

admin.site.register(Post,PostAdmin)
# admin.site.register(Comment)
admin.site.register(ActionHistory, ActionHistoryAdmin)
admin.site.register(ActivityHistory, ActivityHistoryAdmin)

