from django.urls import path
from blog import views
urlpatterns = [
    path('', views.add_blogs, name="addblog"),
#    path('statistics/', views.statistics_view, name="statistics"),

]   