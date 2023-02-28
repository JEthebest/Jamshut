from django import forms
from .models import Location, Product

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['id', 'location_name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'product_name']