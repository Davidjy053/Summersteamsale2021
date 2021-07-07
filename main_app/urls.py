from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sales/', views.index, name='index'),
    path('sales/<int:sales_id>/', views.sale_detail, name='detail'),
    path('sales/create/', views.SalesCreate.as_view(), name='sales_create'),
    path('sales/<int:pk>/update/', views.SalesUpdate.as_view(), name='sales_update'),
    path('sales/<int:pk>/delete/', views.SalesDelete.as_view(), name='sales_delete'),
]