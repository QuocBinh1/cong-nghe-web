from django.contrib import admin
from .models import Comment , Post ,ActionHistory 
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','price','quantity','category','trademark','image' ,'timestamp','total_price_display']
    list_filter = ['timestamp' ,'category', 'trademark']
    search_fields = [ 'title','category', 'trademark']
    readonly_fields = ['total_price_display']
    def total_price_display(self, obj):
        return Post.total_price()
    total_price_display.short_description = 'Total Price'
    inlines = [CommentInline]
    
class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = ('action', 'post_title', 'post_price', 'post_quantity', 'post_category', 'post_trademark','timestamp')
    list_filter = ('action', 'timestamp' , 'post_trademark', 'post_category' ) 
    search_fields = ('post_title', 'action', 'post_trademark', 'post_category' )
    

admin.site.register(Post,PostAdmin)
# admin.site.register(Comment)
admin.site.register(ActionHistory, ActionHistoryAdmin)

