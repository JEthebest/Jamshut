from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('orders/', views.order_list, name='order_list'),
    path('customer/add/', views.customer_create, name='customer_create'),
    path('employee/add/', views.employee_create, name='employee_create'),
    path('order/add/', views.order_create, name='order_create'),
    path('customer/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('order/<int:pk>/edit/', views.order_update, name='order_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('employee/<int:pk>/delete', views.employee_delete, name='employee_delete'),
    path('order/<int:pk>/delete', views.order_delete, name='order_delete'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]