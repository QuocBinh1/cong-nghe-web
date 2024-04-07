from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'news'
urlpatterns = [
    path('' , views.post_list_news , name = 'news'),
    path('<int:id>/' , views.postDetaill , name = 'postDetaill'),
    #path('saveRegister/' , views.saveRegister , name = "saveRegister")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

