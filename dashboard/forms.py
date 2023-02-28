from django import forms
from .models import Customer, Employee, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'age', 'gender', 'location']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'age', 'gender', 'location']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'order_name', 'product', 'amount', 'customer', 'employee', 'date']
