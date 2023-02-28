from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.location_name
    

class Product(models.Model):
    product_name = models.CharField(
        max_length=225, 
        null=True, 
        blank=True, 
        verbose_name='Название продукта'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name