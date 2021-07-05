from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sales/', views.index, name='index'),
    path('sales/<int:sales_id>/', views.sale_detail, name='detail'),
]