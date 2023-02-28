from django.urls import path
from . import views

app_name = 'markets'

urlpatterns = [
    path('', views.markets, name='market'),
    path('lacations/', views.location_list, name='location_list'),
    path('products/', views.product_list, name='product_list'),
    path('location/add/', views.location_create, name='location_create'),
    path('product/add/', views.product_create, name='product_create'),
    path('location/<int:pk>/edit/', views.location_update, name='location_update'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('location/<int:pk>/delete/', views.location_delete, name='location_delete'),
    path('product/<int:pk>/delete', views.product_delete, name='product_delete'),

]