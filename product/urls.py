from django.urls import path
from product import views
urlpatterns = [
    path('', views.add_product, name="addproduct"),
#    path('statistics/', views.statistics_view, name="statistics"),

]   