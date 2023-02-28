from django.db import models
from django.urls import reverse_lazy

from markets.models import Location, Product

GENDER_CHOICES = (
    ('MAN', 'Man'),
    ('WOMAN', 'Woman'),
    ('BI', 'Bi'),
    ('OTHER', 'Other')
)

class Customer(models.Model):
    customer_name = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='Customer name'
    )
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='OTHER'
    )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.customer_name
    
    

class Employee(models.Model):
    employee_name = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='Employee name'
    )
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='OTHER'
    )
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.employee_name
   
    

class Order(models.Model):
    order_name = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='Order name'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE
    )
    date = models.DateField(
        null=True,
        blank=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.order_name
    