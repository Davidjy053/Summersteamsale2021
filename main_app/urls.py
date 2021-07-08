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
    path('sales/<int:sale_id>/add_mod/', views.add_mod, name='add_mod'),
    path('genres/', views.GenresList.as_view(), name='genres_index'),
    path('genres/<int:pk>/', views.GenresDetail.as_view(), name='genres_detail'),
    path('genres/create/', views.GenresCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/update/', views.GenresUpdate.as_view(), name='genres_update'),
    path('genres/<int:pk>/delete/', views.GenresDelete.as_view(), name='genres_delete'),
    path('sales/<int:sale_id>/assoc_genres/<int:genres_id>/', views.assoc_genres, name='assoc_genres'),

]